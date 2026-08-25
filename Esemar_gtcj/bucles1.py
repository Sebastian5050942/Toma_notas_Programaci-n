numero = 10
while numero <= 50:
    if numero % 2 == 0:
        print(numero)
    numero += 1     #numero = numero + 1

# Imprimir los números entre 1000 y 0 en orden descendente que sean múltiplos de 13
numero = 1000
while numero > 0:
    if numero % 13 == 0:
        print(numero)
    numero -= 1     #numero = numero - 1

#Definir un password = "h123-"

password = "h123-"

# Solicitar al usuario que ingrese un password y verificar si es correcto
clave = input("Ingrese el password: ")
if clave == password:
    print("Password correcto.")
else:
    print("Password incorrecto.")

# Si el password es incorrecto, solicitar al usuario que ingrese nuevamente el password hasta que sea correcto
clave = input("Ingrese el password: ")
while clave != password:
    print("Password incorrecto.")
    clave = input("Ingrese el password: ")
print("Password correcto.")

# Contar cuantos intentos fallidos hubo antes de ingresar el password correcto
clave = input("Ingrese el password: ")
intentos = 5
while clave != password:
    print("Password incorrecto.")
    intentos += 1
    clave = input("Ingrese el password: ")
print("Password correcto.")
print(f"Intentos fallidos: {intentos}")