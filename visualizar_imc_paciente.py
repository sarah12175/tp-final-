from datos_globales import datos_pacientes
import pandas as pd 
def visualizar_imc(): 
    datos_filtrados=datos_pacientes
    df=pd.DataFrame(datos_filtrados)
    pd.set_option('display.max_rows', None)
    print(df[['paciente_id','IMC']])