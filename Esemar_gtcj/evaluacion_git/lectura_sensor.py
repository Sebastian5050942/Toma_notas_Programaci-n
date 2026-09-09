import random
import time

def leer_sensor():
    """Simula la lectura de un sensor I2C en un sistema embebido."""
    valor = round(random.uniform(15.0, 35.0), 2)
    return valor

if __name__ == "__main__":
    print("--- Sistema de Monitoreo de Temperatura ---")
    for i in range(5):
        temp = leer_sensor()
        print(f"Muestra [{i+1}/5]: {temp} °C")
        time.sleep(1)
    print("Muestreo finalizado con éxito.")
