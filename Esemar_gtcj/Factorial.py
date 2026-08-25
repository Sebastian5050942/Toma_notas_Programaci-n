# n = int(input("Ingrese el valor:"))
# factorial = 1
# contador = 1
# while contador <= n:
#    factorial = factorial * contador
 #   contador = contador + 1
  #  print(f"{n}! = {factorial}")

    # Ahora utlizando el bucle range

n = int(input("Ingrese el valor:"))
factorial = 1
for cont in range(1, n+1):
    factorial *= cont
    print(f"#{n}! = {factorial}" )
