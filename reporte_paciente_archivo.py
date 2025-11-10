import pandas as pd
from datetime import datetime

def guardar_reporte_en_archivo(datos_pacientes):
    # Obtener fecha y hora actuales
    ahora = datetime.now()
    timestamp = ahora.strftime("%Y%m%d_%H%M%S")  # formato: AAAAMMDD_HHMMSS
    nombre_archivo = f"reporte_pacientes_{timestamp}.txt"

    # Crear DataFrame
    df = pd.DataFrame(datos_pacientes)

    # Abrir archivo en modo escritura
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write("=== Reporte de Pacientes ===\n\n")
        for _, fila in df.iterrows():
            f.write(f"ID: {fila['paciente_id']}\n")
            f.write(f"Nombre: {fila['nombre_paciente']}\n")
            f.write(f"Edad: {fila['edad']}\n")
            f.write(f"Peso: {fila['peso']} kg\n")
            f.write(f"Altura: {fila['altura']} m\n")
            f.write(f"IMC: {fila['IMC']:.2f}\n")
            f.write(f"PAM: {fila['PAM']:.2f}\n")
            f.write(f"Color triage: {fila['color']}\n")
            f.write("-" * 30 + "\n")

    print(f"Reporte guardado correctamente en '{nombre_archivo}'.")
