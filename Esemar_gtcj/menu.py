#1. Platos fuertes  2. Bebidas  3. Postres  4. Salir


# Imprimir el Menú
print("1. Platos fuertes\n2. Bebidas\n3. Postres\n4. Salir")
#Leer la opción
opcion = int(input("Ingrese la opción: "))

while True: #Crea un bucle infinito
    if opcion == 1:
        print("1. Platos fuertes")
        print("1. Punta de anca\n2. Lomo fino\n3. Pollo a la plancha")
        plato = input("Elige una opción: ")
        print("\n\n")
        print(f"Usted eligió: {plato}")
        print("\n\n")
    elif opcion == 2:
        print("2. Bebidas")
        print("1. Soda Saborizada\n2. Jugo Natural\n3. Café")
        bebida = input("Elige una opción: ")
        print("\n\n")
        print(f"Usted eligió: {bebida}")
        print("\n\n")
    elif opcion == 3:
        print("3. Postres")
        print("1. Helado de chocolate\n2. Tarta de manzana\n3. Flan")
        postre = input("Elige una opción: ")
        print("\n\n")
        print(f"Usted eligió: {postre}")
        print("\n\n")
    elif opcion == 4:
        print("4. Saliendo...!")
        break  #Rompe el bucle
    else:
        print("Opción inválida")

# Imprimir el Menú
print("1. Platos fuertes\n2. Bebidas\n3. Postres\n4. Salir")
#Leer la opción
opcion = int(input("Ingrese la opción: "))

