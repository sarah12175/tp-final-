import matplotlib.pyplot as plt 
import numpy as np
from analisis_ecg_paciente import analizar_ecg
# ------------------ GRAFICO DE LINEAS (ECG) ------------------
def grafico_de_lineas():
    # Analizar los archivos ECG y guardarlos en una lista
    ecg_pacientes = analizar_ecg()
    # Pedir al usuario que ingrese un ID 
    paciente_id_elegido=input("Ingrese el ID del paciente para ver su ECG (ej. P0001): ")
    encontrado=False
    for fila in ecg_pacientes: 
        if fila['paciente_id']==paciente_id_elegido: 
            senal=fila['senal']
            plt.figure(figsize=(10,4))
            plt.plot(senal, color='purple')
            plt.title(f'señal ecg del paciente {paciente_id_elegido}')
            plt.xlabel('tiempo (muestras)')
            plt.ylabel('voltaje(mv)')
            plt.show()
            encontrado=True 
            break 
    if not encontrado: 
        print("No se encontro al paciente en la lista")
       
