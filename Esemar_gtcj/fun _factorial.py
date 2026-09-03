
def factorial(n):
    fac = 1
    for cont in range(1 + n+1):
        fac *= cont         #factorial = factorial * contador
    return fac






#Programa principal
num = int(input("Ingrese el valor"))
resul = factorial(num)

print(f"{num}! = {resul}")

