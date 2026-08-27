num = int(input("Número a evaluar: "))
cont = 0

for i in range(2, num, 1):
    if (num % i) == 0:
        cont += 1

if cont == 0:
    print(f"{num} es un número primo")
else:
    print(f"{num} no es un número primo")