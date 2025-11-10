import csv
from clasificacion_triage import *
def verificar_paciente_id(paciente_id):#verificar si esta correcto paciente_id 
    if len(paciente_id)!=5: 
        return False
    if paciente_id[0]!='P': 
        return False 
    for i in range(1,5,1): 
        if not paciente_id[i].isdigit():
            return False
    return paciente_id
def verificar_nombre(nombre): 
    if nombre=='' or nombre is None: 
        return None 
    #limpiar el texto 
    nombre= nombre.strip().lower()
    if nombre.replace(" ","").isalpha(): 
        return nombre
    else: 
        return False 
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
    
    #caso especial para los muertos 
    if palabras_validas==['lpm','frecuenciacardiaca','frecuencia']: 
        if valor==0: 
            return 0 
        elif minimo<= valor <=maximo: 
            return valor 
        else: 
            return False 
        
    # verificar rango
    if minimo <= valor <= maximo:
        return valor
    else:
        return False 
    
def verificar_valor_presion(valor_principal, valor_secundario, palabras_validas, minimo, maximo):
    if valor_principal=='' or valor_principal is None: 
        return None 
    if valor_secundario=='' or valor_secundario is None: 
        return None 
    
    #limpiar el texto 
    valor_principal=valor_principal.replace(' ','').lower()
    valor_secundario=valor_secundario.replace(' ','').lower()

    # quitar las palabras válidas de valor_principal si las tiene
    for p in palabras_validas:
        if valor_principal.startswith(p):
            valor_principal = valor_principal[len(p):]
            break
        elif valor_principal.endswith(p):
            valor_principal= valor_principal[:-len(p)]
            break 

    # quitar las palabras válidas de valor_secundario si las tiene
    for p in palabras_validas:
        if valor_secundario.startswith(p):
            valor_secundario = valor_secundario[len(p):]
            break
        elif valor_secundario.endswith(p):
            valor_secundario= valor_secundario[:-len(p)]
            break 

    #convertir a numero 
    try:  
        valor_principal=int(valor_principal)
        valor_secundario=int(valor_secundario)
    except ValueError: 
        return None 
    
    #caso especial en que valor sea igual a cero 
    if valor_principal==0 and valor_secundario==0: 
        return 0 
    
    #verificar rango 
    if (minimo <=valor_principal<=maximo):
        return valor_principal 
    else: 
        return False 
    
def calcular_IMC(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def calcular_PAM(sistolica, diastolica):
    if sistolica==0 and diastolica==0: 
        return 0
    else: 
        pam = (sistolica+2*diastolica)/3
        return pam 

def calcular_oximetria_de_pulso(pulsoximetro_ir_perc,pulsoximetro_r_perc):
   oximetria=100 * (pulsoximetro_ir_perc /(pulsoximetro_r_perc + pulsoximetro_ir_perc))
   return oximetria 

def calcular_RCG(glucosa,colesterol):
    RCG=glucosa/colesterol
    
    return RCG

def analisis_pacientes(): 
    with open('pacientes_final.csv','r',encoding='utf-8-sig') as file: #abro el archivo para leerlo 
        lector=csv.DictReader(file) 
        datos_pacientes=list(lector) #guardo el archivo en una lista de diccionarios 
        datos_filtrados=[]
        for fila in datos_pacientes:
            paciente_id=verificar_paciente_id(fila['paciente_id'])
            nombre=verificar_nombre(fila['nombre_paciente'])
            edad=verificar_valor(fila['edad'], palabras_validas=['ano','anos'], tipo='int', minimo=0, maximo=120)
            peso=verificar_valor(fila['peso_kg'],['kg','peso','k'], 'float',0.0,500.0)
            altura=verificar_valor(fila['altura_m'],['m','altura','metros'],'float',0.25,2.7)
            sistolica=verificar_valor_presion(fila['sistolica_mmHg'],fila['diastolica_mmHg'],['mmhg','presion'],40,250)
            diastolica=verificar_valor_presion(fila['diastolica_mmHg'],fila['sistolica_mmHg'],['mmhg','presion'],20,150)
            temperatura=verificar_valor(fila['temperatura_C'],['°c','temperatura','c'],'float',25.0,45.0)
            frecuencia= verificar_valor(fila['frecuencia_cardiaca_lpm'],['lpm','frecuenciacardiaca','frecuencia'],'int',30,300)
            nivel_oxigeno=verificar_valor(fila['nivel_oxigeno_perc'],['%','niveloxigeno','oxigeno'],'int',50,100)
            glucosa=verificar_valor(fila['glucosa_mg_dL'],['glucosa','mg/dl','mgdl'],'int',20,1000)
            colesterol=verificar_valor(fila['colesterol_mg_dL'],['colesterol','mg/dl','mgdl'],'int',50,500)
            pulsoximetro_r=verificar_valor(fila['pulsoximetro_r_perc'],['%','pulsoximetro'],'int',50,100)
            pulsoximetro_ir=verificar_valor(fila['pulsoximetro_ir_perc'],['%','pulsoximetro'],'int',50,100)

            if all (x is not None and x is not False for x in[paciente_id,nombre,edad,peso,altura,sistolica,diastolica,temperatura,frecuencia,nivel_oxigeno,glucosa,colesterol,pulsoximetro_r,pulsoximetro_ir]): #la funcion all devuelve true si en la lista no hay False,none,''.
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




