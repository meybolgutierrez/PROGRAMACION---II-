import time      # Librería para trabajar con el tiempo
import random    # Librería para generar números aleatorios

class Cronometro:

    # Constructor de la clase
    def __init__(self):
        self.__inicia = time.time()  # Guarda el tiempo inicial
        self.__finaliza = 0          # Tiempo final inicialmente en 0
    def getInicia(self):
        return self.__inicia
    def getFinaliza(self):
        return self.__finaliza
    def inicia(self):
        self.__inicia = time.time()
    def detener(self):
        self.__finaliza = time.time()
    def lapsoDeTiempo(self):
        return (self.__finaliza - self.__inicia) * 1000

# Función para ordenar los números mediante selección
def ordenamientoSeleccion(numeros):
    n = len(numeros)

    for i in range(n - 1):
        menor = i

        # Busca el número menor
        for j in range(i + 1, n):
            if numeros[j] < numeros[menor]:
                menor = j

        # Intercambia las posiciones
        numeros[i], numeros[menor] = numeros[menor], numeros[i]

# Lista donde se guardarán los números
numeros = []

# Genera 100000 números aleatorios
for i in range(100000):
    numeros.append(random.randint(1, 100000))

# Crea un objeto de la clase Cronometro
cronometro = Cronometro()
cronometro.inicia()
ordenamientoSeleccion(numeros)
cronometro.detener()
print("Tiempo de ejecución:")
print(cronometro.lapsoDeTiempo(), "milisegundos")