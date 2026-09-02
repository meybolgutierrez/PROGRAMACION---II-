import math  
class Estadistica:

    # Constructor
    def __init__(self, datos):
        self.__datos = datos

    # Método que calcula el promedio
    def promedio(self):
        suma = 0

        for numero in self.__datos:
            suma = suma + numero

        return suma / len(self.__datos)

    # Método que calcula la desviación estándar muestral
    def desviacion(self):
        prom = self.promedio()
        suma = 0

        for numero in self.__datos:
            suma = suma + (numero - prom) ** 2

        return math.sqrt(suma / (len(self.__datos) - 1))

# Entrada de los 10 números
datos = list(map(float, input("Ingrese 10 números: ").split()))

estadistica = Estadistica(datos)

print(f"El promedio es {estadistica.promedio():.2f}")
print(f"La desviación estandard es {estadistica.desviacion():.5f}")