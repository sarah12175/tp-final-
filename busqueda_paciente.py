import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from datos_globales import datos_pacientes 

# Función que ejecuta la búsqueda
def buscar_paciente(identificacion):
    encontrado= False 
    for fila in datos_pacientes:
        if fila['paciente_id']==identificacion or identificacion.lower() in fila['nombre_paciente'].lower():  
            print(fila)
            encontrado=True
    if not encontrado: 
        print("El paciente no se encuentra en la lista")
    

    

      
    
    