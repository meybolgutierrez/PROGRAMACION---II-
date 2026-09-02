import math  
def promedio(datos):
    suma = 0
    for numero in datos:
        suma = suma + numero
    return suma / len(datos)
# Función que calcula la desviación estándar muestral
def desviacion(datos):
    prom = promedio(datos)
    suma = 0
    for numero in datos:
        suma = suma + (numero - prom) ** 2
    return math.sqrt(suma / (len(datos) - 1))
# Entrada de los 10 números
datos = list(map(float, input("Ingrese 10 números: ").split()))

print(f"El promedio es {promedio(datos):.2f}")
print(f"La desviación estandard es {desviacion(datos):.5f}")