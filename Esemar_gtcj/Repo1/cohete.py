# Crear la función calcular_altitud.
# Debe llamarse calcular_altitud y recibir solamente presion_hpa como parámetro.
# Calcular la altitud usando exactamente esta fórmula:
# h = 44330 * (1 - (presion_hpa / 1013.25) ** 0.1903)
# Retornar la altitud calculada

def calcular_altitud(presion_hpa):
    h = 44330 * (1 - (presion_hpa / 1013.25) ** 0.1903)
    return h

# Crear la función determinar_estado_vuelo.
# Debe recibir exactamente estos tres parámetros:
# altitud_actual, altitud_previa y aceleracion.
# Si altitud_actual es mayor que altitud_previa, retornar 1 para Ascenso.
# Si no está ascendiendo, evaluar las condiciones del reto para retornar
# 2 para Apogeo/Caída libre o 3 para Despliegue de Paracaídas.
# No inventar valores de altitud ni nombres de estados.

def determinar_estado_vuelo(altitud_actual, altitud_previa, aceleracion):
    if altitud_actual > altitud_previa:
        return 1
    elif aceleracion < 0:
        return 2
    else:
        return 3

# Crear la función evaluar_alerta_temperatura.
# Debe recibir temp_celsius como parámetro.
# Si la temperatura supera el límite crítico, retornar True.
# Si no lo supera, retornar False.

def evaluar_alerta_temperatura(temp_celsius):
    limite_critico = 100  # Valor provisional
    if temp_celsius > limite_critico:
        return True
    else:
        return False

# Crear la función main que controle el monitoreo del vuelo.
# Inicializar las variables necesarias para tiempo, altitud previa,
# altitud máxima, apogeo, temperatura acumulada, cantidad de lecturas,
# aceleración máxima y estado de la simulación.
# Utilizar un ciclo while mientras la simulación esté activa.

def main():
    tiempo = 0
    altitud_previa = 0
    altitud_maxima = 0
    apogeo_detectado = False
    temperatura_acumulada = 0
    cantidad_lecturas = 0
    aceleracion_maxima = 0
    simulacion_activa = True

    while simulacion_activa:
        presion_hpa = float(input("Ingrese la presión atmosférica (hPa): "))
        temp_celsius = float(input("Ingrese la temperatura (°C): "))
        aceleracion = float(input("Ingrese la aceleración (m/s²): "))

        altitud_actual = calcular_altitud(presion_hpa)
        print(f"Altitud actual: {altitud_actual} m")
        estado_vuelo = determinar_estado_vuelo(
            altitud_actual,
            altitud_previa,
            aceleracion
        )

        if estado_vuelo == 1:
            print("Estado: Ascenso")
        elif estado_vuelo == 2:
            print("Estado: Apogeo/Caída libre")
        else:
            print("Estado: Despliegue de Paracaídas")

        if altitud_actual > altitud_maxima:
            altitud_maxima = altitud_actual

        if  altitud_actual < altitud_previa and apogeo_detectado == False:
            apogeo_detectado = True
            print("Apogeo detectado")

        if evaluar_alerta_temperatura(temp_celsius):
            print("Alerta: Temperatura crítica alcanzada!")

        temperatura_acumulada += temp_celsius
        cantidad_lecturas += 1

        if aceleracion > aceleracion_maxima:
            aceleracion_maxima = aceleracion

        altitud_previa = altitud_actual
        tiempo += 1

        if altitud_actual <= 0:

            simulacion_activa = False

    print(f"Altitud máxima alcanzada: {altitud_maxima} m")
    print(f"Temperatura promedio: {temperatura_acumulada / cantidad_lecturas} °C")
    print(f"Aceleración máxima: {aceleracion_maxima} m/s²")

main()

