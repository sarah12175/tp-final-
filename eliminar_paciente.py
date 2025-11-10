from datos_globales import datos_pacientes 
def eliminar_paciente(paciente): 
    encontrado=False
    for i in datos_pacientes: 
        if paciente==i['paciente_id']: 
            datos_pacientes.remove(i) #elimina la fila de la lista global 
            print("Paciente eliminado")
            encontrado=True
            break
    if not encontrado: 
        print("El paciente no se encuentra en la lista")