from math import sqrt
class MiPunto:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def distancia(self, p=None, x=None, y=None):
        if p != None:
            dx = self.__x - p.getX()
            dy = self.__y - p.getY()
        else:
            dx = self.__x - x
            dy = self.__y - y
        return sqrt(dx ** 2 + dy ** 2)
    def __str__(self):
        return "(" + str(self.__x) + ", " + str(self.__y) + ")"

p1 = MiPunto()
p2 = MiPunto(10, 30.5)

print("Punto 1:", p1)
print("Punto 2:", p2)
print("Distancia:", p1.distancia(p2))
print("Distancia:", p1.distancia(x=10, y=30.5))