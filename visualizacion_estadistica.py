from datos_globales import datos_pacientes
import pandas as pd 
def estadisticas_generales():
    datos_filtrados=datos_pacientes 
    df=pd.DataFrame(datos_filtrados)
    print("=== Estadísticas Generales de Pacientes ===")
    print(f"Cantidad total de pacientes: {len(df)}")
    print("\nCantidad de pacientes por triage:")
    print(df['color'].value_counts())
    print("\nPromedios:")
    print(f"Edad promedio: {df['edad'].mean():.2f}")
    print(f"Peso promedio: {df['peso'].mean():.2f}")
    print(f"IMC promedio: {df['IMC'].mean():.2f}")
    print(f"PAM promedio: {df['PAM'].mean():.2f}")

