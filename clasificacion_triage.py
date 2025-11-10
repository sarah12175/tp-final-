def clasificar_triage(paciente):
    
    """
    Clasifica al paciente según el triage de 6 colores.
    Recibe un diccionario con datos del paciente y devuelve un string con el color.
    """
    
    temp = paciente["temperatura_C"]
    fc = paciente["frecuencia_cardiaca_lpm"]
    spo2 = paciente["nivel_oxigeno_perc"]
    pam = paciente["PAM"] #presion arterial media
    imc = paciente["IMC"]
    glucosa = paciente["glucosa_mg_dL"]
    colesterol = paciente["colesterol_mg_dL"]
    rgc = paciente["RGC"]

    #negro(paciente muerto)
    if fc==0 and pam==0:
        return "negro"

    #rojo(emergencia crtica)
    if temp>39.5 or spo2<85 or pam<60 or pam>120:
        return "rojo"

    #naranja(requiere atencion urgente)
    if (38.5<=temp<=39.5)or (fc > 120 or fc < 50) or (85 <= spo2 <= 92) or (imc > 40):
        return "naranja"
    
    #amarillo(necesita seguimiento)
    if (37.5 <= temp < 38.5) or (glucosa > 180) or (colesterol > 240):
       return "amarillo"

    #verde(saludable con precaucion)
    if (25<=imc<=30)or(rgc>1):
       return "verde"

    #azul(saludable)
    return "azul"