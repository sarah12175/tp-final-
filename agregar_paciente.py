from analizar_paciente import * 
from datos_globales import datos_pacientes
def agregar_paciente(): 
    agregado={}
    #ID del paciente
    while True: 
        paciente_id=input("Ingrese ID del paciente: ")
        paciente_id=verificar_paciente_id(paciente_id)
        if paciente_id != False and paciente_id is not None:
            existe= False 
            #verificar si el id ya esta en los datos 
            for fila in datos_pacientes: 
                if paciente_id==fila['paciente_id']: 
                     existe=True 
                     while True: 
                        respuesta=input("Este ID ya se encuentra registrado en el sistema. Esta seguro que quiere cambiarlo? Responda con si o no ")
                        if respuesta.lower()=='si': 
                          agregado['paciente_id']=paciente_id
                          print("ID actualizado correctamente. ")
                          break  
                        elif respuesta.lower()=='no':
                             print("Operacion cancelada. Volviendo al menu principal...")
                             return 
                        else: 
                             print("Respuesta no valida. Escriba 'si' o 'no'")
                     break 
            if not existe: 
                 agregado['paciente_id']=paciente_id
            break 
                       
        else: 
             print('Hubo un error en el dato que ingreso.')

    #Nombre del paciente 
    while True: 
        nombre=input("Ingrese nombre del paciente: ")
        nombre=verificar_nombre(nombre)
        if nombre!=False and nombre is not None: 
             agregado['nombre_paciente']=nombre
             break 
        else: 
             print("Hubo un error en el dato que ingreso. ")

    #Edad del paciente
    while True: 
        edad=input("Ingrese la edad del paciente: ")
        edad=verificar_valor(edad,['ano','anos'],'int', 0, 120)
        if edad is not False and edad is not None: 
             agregado['edad']=edad
             break
        else: 
             print("Hubo un error en el dato que ingreso.")

    #Peso del paciente 
    while True: 
        peso=input("Ingrese el peso del paciente: ")
        peso=verificar_valor(peso,['kg','peso','k'], 'float',0.0,500.0)
        if peso!=False and peso is not None: 
             agregado['peso_kg']=peso
             break
        else: 
             print("Hubo un error en el dato que ingreso. ")

    #Altura del paciente
    while True: 
        altura=input("Ingrese la altura del paciente: ")
        altura=verificar_valor(altura,['m','altura','metros'],'float',0.25,2.7)
        if altura!=False and altura is not None: 
             agregado['altura_m']=altura
             break 
        else: 
             print("Hubo un error en el dato que ingreso. ")

    #Sistolica y diastolica del paciente
    while True: 
        sistolica=input("Ingrese la presion sistolica del paciente: ")
        diastolica=input("Ingrese la presion diastolica del paciente: ")
        sistolica_revisada=verificar_valor_presion(sistolica, diastolica,['mmhg','presion'],40,250)
        diastolica_revisada=verificar_valor_presion(diastolica,sistolica,['mmhg','presion'],20,150)
        if (sistolica_revisada!=False and sistolica_revisada is not None) and (diastolica_revisada!=False and diastolica_revisada is not None): 
             agregado['sistolica_mmHg']=sistolica_revisada 
             agregado['diastolica_mmHg']=diastolica_revisada 
             break 
        else: 
             print("Hubo un error en los datos que ingreso. ")
    
    #Temperatura del paciente 
    while True: 
        temperatura= input("Ingrese la temperatura del paciente: ")
        temperatura=verificar_valor(temperatura,['°c','temperatura','c'],'float',25.0,45.0)
        if temperatura!=False and temperatura is not None: 
             agregado['temperatura_C']=temperatura 
             break 
        else: 
             print("Hubo un error en el dato que ingreso")

    #Frecuencia cardiaca del paciente 
    while True: 
        frecuencia_cardiaca= input("Ingrese la frecuencia cardiaca del paciente: ")
        frecuencia_cardiaca=verificar_valor(frecuencia_cardiaca,['lpm','frecuenciacardiaca','frecuencia'],'int',0,300)
        if frecuencia_cardiaca!=False and frecuencia_cardiaca is not None: 
             agregado['frecuencia_cardiaca_lpm']=frecuencia_cardiaca 
             break 
        else: 
             print("Hubo un error en el dato que ingreso. ")
    
    #Nivel de oxigeno del paciente 
    while True: 
        nivel_oxigeno=input("Ingrese el nivel de oxigeno del paciente: ")
        nivel_oxigeno=verificar_valor(nivel_oxigeno,['%','niveloxigeno','oxigeno'],'int',50,100)
        if nivel_oxigeno!=False and nivel_oxigeno is not None: 
             agregado['nivel_oxigeno_perc']=nivel_oxigeno 
             break
        else: 
             print("Hubo un error en el dato que ingreso. ")

    #Glucosa del paciente 
    while True: 
        glucosa=input("Ingrese la glucosa del paciente: ")
        glucosa=verificar_valor(glucosa,['glucosa','mg/dl','mgdl'],'int',20,1000)
        if glucosa!=False and glucosa is not None: 
             agregado['glucosa_mg_dL']=glucosa
             break
        else: 
             print("Hubo un error en el dato que ingreso. ")

    #Colesterol del paciente 
    while True: 
        colesterol=input("Ingrese el colesterol del paciente: ")
        colesterol=verificar_valor(colesterol,['colesterol','mg/dl','mgdl'],'int',50,500)
        if colesterol!=False and colesterol is not None: 
             agregado['colesterol_mg_dL']=colesterol 
             break
        else: 
             print("Hubo un error en el dato que ingreso. ")

    #Pulsoximetro derecho del paciente 
    while True: 
        pulsoximetro_r=input("Ingrese el pulsoximetro derecho del paciente: ")
        pulsoximetro_r=verificar_valor(pulsoximetro_r,['%','pulsoximetro'],'int',50,100)
        if pulsoximetro_r!=False and pulsoximetro_r is not None: 
             agregado['pulsoximetro_r_perc']=pulsoximetro_r 
             break
        else: 
             print("Hubo un error en el dato que ingreso. ")

    #Pulsoximetro izquierdo del paciente 
    while True: 
        pulsoximetro_ir=input("Ingrese el pulsoximetro izquierdo del paciente: ")
        pulsoximetro_ir=verificar_valor(pulsoximetro_ir,['%','pulsoximetro'],'int',50,100)
        if pulsoximetro_ir!=False and pulsoximetro_ir is not None: 
             agregado['pulsoximetro_ir_perc']=pulsoximetro_ir
             break
        else: 
             print("Hubo un error en el dato que ingreso. ")
    
    #agregar las cuatro columnas nuevas 
    agregado['IMC']=calcular_IMC(agregado['peso_kg'],agregado['altura_m'])
    agregado['PAM']=calcular_PAM(agregado['sistolica_mmHg'],agregado['diastolica_mmHg'])
    agregado['oximetria_de_pulso']=calcular_oximetria_de_pulso(agregado['pulsoximetro_ir_perc'],agregado['pulsoximetro_r_perc'])
    agregado['RGC']=calcular_RCG(agregado['glucosa_mg_dL'],agregado['colesterol_mg_dL'])
    agregado['color']=clasificar_triage(agregado)
   
    for i, fila in enumerate(datos_pacientes):
        if fila['paciente_id'] == agregado['paciente_id']:
            datos_pacientes[i] = agregado  # reemplaza toda la fila
            return datos_pacientes 
    datos_pacientes.append(agregado)
    return datos_pacientes 

              
 

    