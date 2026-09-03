import random



#Generar 10 números aleatorios entre 0 y 100
print("Enteros \t Flotantes")
print("_"*20)
for i in range(10):
    aleatorio = random.radiant(0,100)
    flotante = random.uniform(0.0,5.0)
    print(f"{aleatorio} \t {flotante:0.4}")


