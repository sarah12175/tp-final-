import matplotlib.pyplot as plt
from datos_globales import datos_pacientes
from clasificacion_triage import clasificar_triage
import pandas as pd 
# ------------------ GRAFICO DE DISPERSION ------------------
def grafico_de_dispersion(): 
    # Crear un DataFrame con los pacientes validados
    datos_filtrados=datos_pacientes
    df = pd.DataFrame(datos_filtrados)

    colores_map = {
        "negro": "black",
        "rojo": "red",
        "naranja": "orange",
        "amarillo": "yellow",
        "verde": "green",
        "azul": "blue"
    }

    plt.figure(figsize=(8,6))
    for color in df['color'].unique():
        subset=df[df['color']==color]
        plt.scatter(subset['IMC'],subset['PAM'], c=colores_map[color], label=color, alpha=0.7)

    plt.title('Relación entre IMC y PAM por Clasificación de Triage')
    plt.xlabel('IMC (Índice de Masa Corporal)')
    plt.ylabel('PAM (Presión Arterial Media)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()
    