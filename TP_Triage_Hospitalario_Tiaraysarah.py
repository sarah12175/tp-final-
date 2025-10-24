import sys
import csv
import math
from typing import Dict, List, Any, Tuple, Optional


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#pandas: manejar tablas (CSV), numpy: cálculos numéricos, matplotlib: hacer gráficos, os: manejar archivos en carpetas

#vamos a tener un archivo pacientes_final.csv con columnas como:id, nombre, apellido, edad, peso, altura, presion_sistolica, presion_diastolica, spo2, frecuencia_cardiaca

pacientes = pd.read_csv("pacientes_final.csv") #para leer los archivos
print(pacientes.head())

#calcular las indicaciones IMC Y PAM

    pacientes["IMC"] = pacientes["peso"] / (pacientes["altura"] ** 2)
    pacientes["PAM"] = (pacientes["presion_sistolica"] + 2 * pacientes["presion_diastolica"]) / 3

#calcular oximetria de pulso

   pacientes["spO2_calc"]=100 * (pacientes["pulsioximetro_ir_perc"] /(pacientes["pulsioximetro_r_perc"] + pacientes["pulsioximetro_ir_perc"]))

#calcular la relacion glucosa-colesterol

    pacientes["RGC"]=pacientes["glucosa"]/pacientes["colesterol"]

return pacientes

#row es la variable que recibe la función; representa una "fila" con los valores necesarios (por ejemplo, "spo2", "frecuencia_cardiaca", "PAM", "IMC").

# Función para clasificar el triage según los valores del paciente
def clasificar_triage(row):
    if row["spo2"] < 80 or row["frecuencia_cardiaca"] < 30:
        return "Negro"
    elif row["spo2"] < 85 or row["frecuencia_cardiaca"] > 150:
        return "Rojo"
    elif row["spo2"] < 90 or row["PAM"] < 70:
        return "Naranja"
    elif row["PAM"] < 80 or row["IMC"] > 30:
        return "Amarillo"
    else:
        return "Verde"

# Aplicamos la función a cada fila
pacientes["Triage"] = pacientes.apply(clasificar_triage, axis=1)

# Guardamos el nuevo archivo con los cálculos
pacientes.to_csv("pacientes_procesados.csv", index=False)
print("\nArchivo 'pacientes_procesados.csv' guardado con éxito.")

# Mostramos el gráfico inicial
conteo = pacientes["Triage"].value_counts()
conteo.plot(kind="bar", color=["black", "red", "orange", "yellow", "green"])
plt.title("Cantidad de pacientes por triage")
plt.xlabel("Color")
plt.ylabel("Cantidad")
plt.show()

# Menú interactivo
while True:
    print("\n--- MENÚ TRIAGE ---")
    print("1. Ver primeros pacientes")
    print("2. Buscar por apellido")
    print("3. Guardar archivo procesado")
    print("4. Ver gráfico de triage")
    print("5. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        print(pacientes.head())

    elif opcion == "2":
        ape = input("Apellido: ").capitalize()
        print(pacientes[pacientes["apellido"] == ape])

    elif opcion == "3":
        pacientes.to_csv("pacientes_procesados.csv", index=False)
        print("Archivo guardado correctamente.")

    elif opcion == "4":
        conteo = pacientes["Triage"].value_counts()
        conteo.plot(kind="bar", color=["black", "red", "orange", "yellow", "green"])
        plt.show()

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida.")