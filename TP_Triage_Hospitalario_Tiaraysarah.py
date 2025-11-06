import sys
import csv
import math
from typing import Dict, List, Any, Tuple, Optional
import tkinter as tk 


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

BASE_CSV = "pacientes_final.csv"        # archivo esperado con pacientes
ECG_MANIFEST = "ecg_manifest.csv"       # opcional: lista de ecg (paciente_id;ecg_file) -> delimitador ; o ajustar
OUTPUT_PROCESSED = "pacientes_procesados.csv"


#pandas: manejar tablas (CSV), numpy: cálculos numéricos, matplotlib: hacer gráficos, os: manejar archivos en carpetas

#vamos a tener un archivo pacientes_final.csv con columnas como:id, nombre, apellido, edad, peso, altura, presion_sistolica, presion_diastolica, spo2, frecuencia_cardiaca
#ecg es archivo csv 

def verificar_paciente_id(paciente_id):#verificar si esta correcto paciente_id 
    if len(paciente_id)!=5: 
        return False
    if paciente_id[0]!='P': 
        return False 
    for i in range(1,5,1): 
        if not paciente_id[i].isdigit():
            return False
    return paciente_id

def verificar_valor(valor, palabras_validas, tipo, minimo, maximo): 
    if valor == '' or valor is None:
        return None

    # limpiar texto
    valor = valor.replace(' ', '').lower().replace(',', '.').replace('ñ', 'n')
    
    # quitar las palabras válidas si las tiene
    for p in palabras_validas:
        if valor.startswith(p):
            valor = valor[len(p):]
            break
        elif valor.endswith(p):
            valor = valor[:-len(p)]
            break

    # convertir a número
    try:
        if tipo == 'int':
            valor = int(valor)
        elif tipo == 'float':
            valor = float(valor)
    except ValueError:
        return None

    # verificar rango
    if minimo <= valor <= maximo:
        return valor
    else:
        return False 

def calcular_IMC(peso, altura):

    imc = peso / (altura ** 2)
    return imc
def calcular_PAM(sistolica, diastolica):
    pam = (sistolica+2*diastolica)/3
    return pam 

def calcular_oximetria_de_pulso(pulsoximetro_ir_perc,pulsoximetro_r_perc):

   oximetria=100 * (pulsoximetro_ir_perc /(pulsoximetro_r_perc + pulsoximetro_ir_perc))
   return oximetria 

def calcular_RCG(glucosa,colesterol):
    RCG=glucosa/colesterol
    return RCG

# Función para clasificar el triage según los valores del paciente
def clasificar_triage(paciente):
    
    """
    Clasifica al paciente según el triage de 6 colores.
    Recibe un diccionario con datos del paciente y devuelve un string con el color.
    """
    
    temp = paciente["temperatura_C"]
    fc = paciente["frecuencia_cardiaca_lpm"]
    spo2 = paciente["nivel_oxigeno_perc"]
    pam = paciente["PAM"] #presion arterial media
    imc = paciente["IMC"]
    glucosa = paciente["glucosa_mg_dL"]
    colesterol = paciente["colesterol_mg_dL"]
    rgc = paciente["RGC"]

    #negro(paciente muerto)
    if fc==0 and pam==0:
        return "negro"

    #rojo(emergencia crtica)
    if temp>39.5 or spo2<85 or pam<60 or pam>120:
        return "rojo"

    #naranja(requiere atencion urgente)
    if (38.5<=temp<=39.5)or (fc > 120 or fc < 50) or (85 <= spo2 <= 92) or (imc > 40):
        return "naranja"
    
    #amarillo(necesita seguimiento)
    if (37.5 <= temp < 38.5) or (glucosa > 180) or (colesterol > 240):
       return "amarillo"

    #verde(saludable con precaucion)
    if (25<=imc<=30)or(rgc>1):
       return "verde"

    #azul(saludable)
    return "azul"


def analisis_pacientes(): 
 with open("pacientes_final.csv",'r',encoding='utf-8-sig') as file: #abro el archivo para leerlo 
    lector=csv.DictReader(file) 
    datos_pacientes=list(lector) #guardo el archivo en una lista de diccionarios 
    datos_filtrados=[]
    for fila in datos_pacientes:
        paciente_id=verificar_paciente_id(fila['paciente_id'])
        nombre=fila['nombre_paciente']
        edad=verificar_valor(fila['edad'], palabras_validas=['ano','anos'], tipo='int', minimo=0, maximo=120)
        peso=verificar_valor(fila['peso_kg'],['kg','peso','k'], 'float',0.0,500.0)
        altura=verificar_valor(fila['altura_m'],['m','altura','metros'],'float',0.25,2.7)
        sistolica=verificar_valor(fila['sistolica_mmHg'],['mmhg','presion'],'int',40,250)
        diastolica=verificar_valor(fila['diastolica_mmHg'],['mmhg','presion'],'int',20,150)
        temperatura=verificar_valor(fila['temperatura_C'],['°c','temperatura','c'],'float',25.0,45.0)
        frecuencia= verificar_valor(fila['frecuencia_cardiaca_lpm'],['lpm','frecuenciacardiaca','frecuencia'],'int',0,300)
        nivel_oxigeno=verificar_valor(fila['nivel_oxigeno_perc'],['%','niveloxigeno','oxigeno'],'int',50,100)
        glucosa=verificar_valor(fila['glucosa_mg_dL'],['glucosa','mg/dl','mgdl'],'int',20,1000)
        colesterol=verificar_valor(fila['colesterol_mg_dL'],['colesterol','mg/dl','mgdl'],'int',50,500)
        pulsoximetro_r=verificar_valor(fila['pulsoximetro_r_perc'],['%','pulsoximetro'],'int',50,100)
        pulsoximetro_ir=verificar_valor(fila['pulsoximetro_ir_perc'],['%','pulsoximetro'],'int',50,100)
        if all ([paciente_id,edad,peso,altura,sistolica,diastolica,temperatura,frecuencia,nivel_oxigeno,glucosa,colesterol,pulsoximetro_r,pulsoximetro_ir]): #la funcion all devuelve true si en la lista no hay False, 0,none,''. 
            fila['paciente_id']=paciente_id
            fila['nombre_paciente']=nombre
            fila['edad']=edad
            fila['peso']=peso
            fila['altura']=altura
            fila['sistolica_mmHg']=sistolica
            fila['diastolica_mmHg']=diastolica
            fila['temperatura_C']=temperatura
            fila['frecuencia_cardiaca_lpm']=frecuencia
            fila['nivel_oxigeno_perc']=nivel_oxigeno
            fila['glucosa_mg_dL']=glucosa
            fila['colesterol_mg_dL']=colesterol
            fila['pulsoximetro_r_perc']=pulsoximetro_r
            fila['pulsoximetro_ir_perc']=pulsoximetro_ir
            #agregar las cuatro columnas nuevas 
            fila['IMC']=calcular_IMC(peso,altura)
            fila['PAM']=calcular_PAM(sistolica,diastolica)
            fila['oximetria_de_pulso']=calcular_oximetria_de_pulso(pulsoximetro_ir,pulsoximetro_r)
            fila['RGC']=calcular_RCG(glucosa,colesterol)
            datos_filtrados.append(fila)
    for paciente in datos_filtrados:
         #agegar una columna nueva que diga color 
         paciente['color']=clasificar_triage(paciente)
    return datos_filtrados 
    

#poner lo de import funciones.py(estas van a ser las funciones que nosotras creamos para que quede mas prolijo)
def analizar_ecg():
    resultados=[]
    with open ("ecg_manifest.csv",'r',encoding='utf-8')as file: #abro el archivo para leerlo 
        lector=csv.DictReader(file)
        ecg_pacientes=list(lector)
        for fila in ecg_pacientes: 
            with open(fila['ecg_file'],'r',encoding='utf-8')as archivo_ecg:
                lector=csv.reader(archivo_ecg)
                lista_senales=[float(linea[0])for linea in lector]
                maximo=max(lista_senales)
                minimo=min(lista_senales)
                promedio=sum(lista_senales)/len(lista_senales)
                resultados.append({'paciente_id':fila['paciente_id'],'maximo':maximo,'minimo':minimo,'promedio':promedio})
    return resultados 


# ------------------ GRAFICO DE BARRAS ------------------
# Crear un DataFrame con los pacientes validados

datos_filtrados=analisis_pacientes()
df = pd.DataFrame(datos_filtrados)

# Aplicar la clasificación del triage y guardarla en una nueva columna
df['Triage'] = df.apply(clasificar_triage, axis=1)

print(df[['temperatura_C', 'frecuencia_cardiaca_lpm', 'nivel_oxigeno_perc', 'PAM', 'IMC']].head())
print(df['Triage'].value_counts())

df.loc[0, ['frecuencia_cardiaca_lpm', 'PAM']] = 0  # Forzamos el primer paciente como muerto
df['Triage'] = df.apply(clasificar_triage, axis=1)

# Contar la cantidad de pacientes por color y ordenarlos del más grave al más leve
orden_colores = ["negro", "rojo", "naranja", "amarillo", "verde", "azul"]
conteo_colores = df['Triage'].value_counts().reindex(orden_colores, fill_value=0)

# Crear el mapa de colores
colores_map = {
    "negro": "black",
    "rojo": "red",
    "naranja": "orange",
    "amarillo": "yellow",
    "verde": "green",
    "azul": "blue"
}

plt.figure(figsize=(8,5))
plt.bar(conteo_colores.index,conteo_colores.values,color=[colores_map.get(c.lower(), "gray") for c in conteo_colores.index])
plt.title('Cantidad de pacientes por categoría de triage')
plt.xlabel('Categoría')
plt.ylabel('Cantidad de pacientes')
plt.grid(axis='y', linestyle="--", alpha=0.6)
plt.show()

# ------------------ GRAFICO DE LINEAS (ECG) ------------------

# Analizar los archivos ECG y guardarlos en una lista
ecg_pacientes = analizar_ecg()

# Ejemplo: mostrar la señal ECG de un paciente específico
paciente_id_elegido=input("Ingrese el ID del paciente para ver su ECG (ej. P0001): ")

#buscar el archivo ECG correspondiente al paciente elegido
paciente_ecg=next((fila for fila in ecg_pacientes if fila['paciente_id']==paciente_id_elegido))

if paciente_ecg:
   ecg_file=paciente_ecg['ecg_file']
   senal=np.loadtxt(ecg_file)
   plt.figure(figsize=(10,4))
   plt.plot(senal, color='violeta')
   plt.title(f'señal ecg del paciente {paciente_id_elegido}')
   plt.xlabel('tiempo (muestras)')
   plt.ylabel('voltaje(mv)')
   plt.show()
else:
    print("no se encontro el archivo ecg para ese paciente")

# ------------------ GRAFICO DE DISPERSION ------------------

colores_map["negro","rojo","naranja","amarillo","verde","azul"]

plt.figure(figsize=(8,6))
for color in df['triage'].unique():
    subset=df[df['triage']==color]
    plt.scatter(subset['IMC'],subset['PAM'], c=colores_map[color], label=color, alpha=0.07)

plt.title('Relación entre IMC y PAM por Clasificación de Triage')
plt.xlabel('IMC (Índice de Masa Corporal)')
plt.ylabel('PAM (Presión Arterial Media)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

#  ------------------ BUSQUEDA DE PACIENTES ------------------
busqueda = input("Ingrese el ID o Apellido del paciente: ").strip().lower()

resultado = df[df['paciente_id'].str.lower().str.contains(busqueda) | df['nombre_paciente'].str.lower().str.contains(busqueda)]

if not resultado.empty:
    print("\n Datos del paciente encontrado:\n")
    print(resultado.to_string(index=False))
else:
    print("No se encontró ningún paciente con ese criterio.")



def main():
    ventana=tk.TK()
    ventana.title("Reporte de datos")
    ventana.geometry("1300x800")
    etiqueta=tk.Label(ventana,text='Hola, buen dia!')
    boton=tk.Button(ventana,text='Presione para ver los datos de los pacientes')
    datos_pacientes=analisis_pacientes() 
    boton.pack()
    for fila in datos_pacientes: 
        print()
    ventana.mainloop()


       










    


    


