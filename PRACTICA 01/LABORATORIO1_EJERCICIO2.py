class EcuacionLineal:
    # Constructor: inicializa los coeficientes como atributos privados
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    # Verifica si el sistema tiene solución
    def tieneSolucion(self):
        return self.__a * self.__d - self.__b * self.__c != 0
    # Calcula el valor de x
    def getX(self):
        return (self.__e * self.__d - self.__b * self.__f) / \
               (self.__a * self.__d - self.__b * self.__c)
    # Calcula el valor de y
    def getY(self):
        return (self.__a * self.__f - self.__e * self.__c) / \
               (self.__a * self.__d - self.__b * self.__c)
# Entrada de los coeficientes
a, b, c, d, e, f = map(float, input("Ingrese a, b, c, d, e, f: ").split())
# Se crea el objeto y se verifica si existe solución
ecuacion = EcuacionLineal(a, b, c, d, e, f)
if ecuacion.tieneSolucion():
    print("x =", ecuacion.getX(), ", y =", ecuacion.getY())
else:
    print("La ecuación no tiene solución")