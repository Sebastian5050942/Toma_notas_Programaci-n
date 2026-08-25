edad = int(input("Ingrese la edad:"))
if edad >= 0:
    if edad < 6:
        etapa = "Infancia"
    elif edad < 12:
        etapa = "Niñez"
    elif edad < 20:
        etapa = "Adolescencia"
    elif edad < 25:
        etapa = "Juventud"
    elif edad < 60:
        etapa = "Adultez"
    else:
        etapa = "Vejez"
    print (f"Usted está en la etapa: {etapa} ")
else:
   print("Edad invalida")