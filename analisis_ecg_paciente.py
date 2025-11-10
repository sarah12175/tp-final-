from datos_globales import datos_pacientes
import csv 
import os 

def analizar_ecg():
    resultados=[]
    
    with open ("ecg_signals/ecg_manifest.csv",'r',encoding='utf-8-sig')as file: #abro el archivo para leerlo 
        lector=csv.DictReader(file)
        ecg_pacientes=list(lector)#guardo el archivo en una lista de diccionarios 
        lista_pacientes=datos_pacientes
        for fila in ecg_pacientes: 
            for i in lista_pacientes: 
                if i['paciente_id']==fila['paciente_id']:
                    ecg_path=os.path.join("ecg_signals",fila["ecg_file"])
                    with open(ecg_path,'r',encoding='utf-8-sig')as archivo_ecg:
                        lector=csv.reader(archivo_ecg)
                        lista_senales=[float(linea[0])for linea in lector]
                        maximo=max(lista_senales)
                        minimo=min(lista_senales)
                        promedio=sum(lista_senales)/len(lista_senales)
                        resultados.append({'paciente_id':fila['paciente_id'],'maximo':maximo,'minimo':minimo,'promedio':promedio,'senal':lista_senales})
                    break; 
    return resultados 