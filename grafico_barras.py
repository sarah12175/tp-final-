import pandas as pd 
import matplotlib.pyplot as plt
from datos_globales import datos_pacientes
 

# ------------------ GRAFICO DE BARRAS ------------------
def grafico_de_barras():
    # Crear un DataFrame con los pacientes validados
    datos_filtrados=datos_pacientes
    df = pd.DataFrame(datos_filtrados)
 
    #Ordenar a los pacientes del más grave al más leve
    orden_colores = ["negro", "rojo", "naranja", "amarillo", "verde", "azul"]
    conteo_colores = df['color'].value_counts().reindex(orden_colores, fill_value=0)

    #Crear el mapa de colores
    colores_map = {
        "negro": "black",
     "rojo": "red",
     "naranja": "orange",
     "amarillo": "yellow",
     "verde": "green",
        "azul": "blue"
    }

    plt.figure(figsize=(8,5))
    plt.bar(conteo_colores.index, conteo_colores.values, color=[colores_map.get(c.lower(), "gray") for c in conteo_colores.index])
    plt.title('Cantidad de pacientes por categoría de triage')
    plt.xlabel('Categoría')
    plt.ylabel('Cantidad de pacientes')
    plt.grid(axis='y', linestyle="--", alpha=0.6)
    # Mostrar la cantidad encima de cada barra
    for i, valor in enumerate(conteo_colores.values):
        plt.text(i, valor + 0.2, str(valor), ha='center', va='bottom')

    plt.show()


