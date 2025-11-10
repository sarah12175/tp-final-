from datos_globales import datos_pacientes 
from grafico_barras import grafico_de_barras 
from grafico_lineas import grafico_de_lineas
from grafico_dispersion import grafico_de_dispersion 
from busqueda_paciente import buscar_paciente 
from eliminar_paciente import eliminar_paciente
from agregar_paciente import agregar_paciente 
from visualizar_imc_paciente import visualizar_imc
from visualizacion_estadistica import estadisticas_generales
from reporte_paciente_archivo import guardar_reporte_en_archivo
import time 
def menu_principal(): 
    while True: 
        print("\n===Bienvenido al MENU PRINCIPAL===")
        print("1.Visualizar el reporte de pacientes")
        print("2.Visualizar el grafico de barras")
        print("3.Visualizar el grafico de lineas de un paciente")
        print("4.Visualizar el grafico de dispersion de un paciente")
        print("5.Buscar paciente por Apellido o Id")
        print("6.Eliminar paciente de la lista")
        print("7.Agregar paciente a la lista")
        print("8.Registrar la cantidad de pacientes totales en el sistema")
        print("9.Visualizar el imc de cada paciente")
        print("10.Visualizar estadisticas generales de los pacientes")
        print("11.Guardar reporte de pacientes en un archivo")
        print("12.Salir")
        opcion=input("Elija una opcion: ")

        if opcion=='1': 
            for fila in datos_pacientes: 
                print(f"ID:{fila['paciente_id']}|Nombre:{fila['nombre_paciente']}|Edad:{fila['edad']}|Peso:{fila['peso_kg']}|Altura:{fila['altura_m']}|Presion sistolica:{fila['sistolica_mmHg']}|Presion distolica:{fila['diastolica_mmHg']}|Temperatura:{fila['temperatura_C']}|Frecuencia cardiaca:{fila['frecuencia_cardiaca_lpm']}|Nivel oxigeno:{fila['nivel_oxigeno_perc']}|Glucosa:{fila['glucosa_mg_dL']}|Colesterol:{fila['colesterol_mg_dL']}|Pulsoximetro_r:{fila['pulsoximetro_r_perc']}|Pulsoximetro_ir:{fila['pulsoximetro_ir_perc']}|IMC:{fila['IMC']}|PAM:{fila['PAM']}|Oximetria de pulso:{fila['oximetria_de_pulso']}|RGC:{fila['RGC']}|Color:{fila['color']}")
            input("Presione ENTER para volver al menu")

        elif opcion=='2': 
            grafico_de_barras()
            input("Presiona ENTER para volver al menu")

        elif opcion=='3': 
            grafico_de_lineas()
            input("Presiona ENTER para volver al menu")

        elif opcion=='4': 
            grafico_de_dispersion()
            input("Presiona ENTER para volver al menu")

        elif opcion=='5': 
            identificacion=input("Ingrese el id o apellido del paciente: ")
            buscar_paciente(identificacion) 
            input("Presiona ENTER para volver al menu")

        elif opcion=='6': 
            paciente=input("Ingrese el id del paciente que desea eliminar: ")
            eliminar_paciente(paciente) 
            input("Presiona ENTER para volver al menu")

        elif opcion=='7': 
            agregar_paciente()
            input("Presiona ENTER para volver al menu")

        elif opcion=='8': 
            cantidad=len(datos_pacientes)
            print("La cantidad de pacientes registrados en el sistema es de ",cantidad)
            input("Presione ENTER para volver al menu")

        elif opcion=='9': 
            visualizar_imc()
            input("Presion ENTER para volver al menu")
        
        elif opcion=='10': 
            estadisticas_generales()
            input("Presione ENTER para volver al menu")

        elif opcion=='11': 
            guardar_reporte_en_archivo(datos_pacientes)
            input("Presione ENTER para volver al menu")

        elif opcion=='12': 
            print("Saliendo del programa...")
            break 

        else: 
            print("Opcion no valida. Intente de nuevo")
            time.sleep(2)

menu_principal()



