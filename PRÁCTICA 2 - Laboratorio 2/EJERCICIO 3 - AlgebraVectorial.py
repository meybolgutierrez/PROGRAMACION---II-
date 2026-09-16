import math
class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getZ(self):
        return self.__z

    def __add__(self, b):
        x = self.__x + b.getX()
        y = self.__y + b.getY()
        z = self.__z + b.getZ()
        return Vector(x, y, z)

    def __mul__(self, b):
        if isinstance(b, Vector):
            return (self.__x * b.getX() + self.__y * b.getY() + self.__z * b.getZ())
        else:
            return Vector(self.__x * b,
                          self.__y * b,
                          self.__z * b)

    def __truediv__(self, r):
        return Vector(self.__x / r, self.__y / r, self.__z / r)

    def longitud(self):
        return math.sqrt(self.__x**2 + self.__y**2 + self.__z**2)

    def normal(self):
        return self / self.longitud()

    def productoVectorial(self, b):
        x = self.__y * b.getZ() - self.__z * b.getY()
        y = self.__z * b.getX() - self.__x * b.getZ()
        z = self.__x * b.getY() - self.__y * b.getX()

        return Vector(x, y, z)

    def __str__(self):
        return "(" + str(float(self.__x)) + ", " + \
                     str(float(self.__y)) + ", " + \
                     str(float(self.__z)) + ")"

a = Vector(1, 2, 3)
b = Vector(4, 5, 6)

print("Vector a:", a)
print("Vector b:", b)
print("Suma:", a + b)
print("Multiplicación por escalar:", a * 2)
print("Longitud de a:", a.longitud())
print("Normal de a:", a.normal())
print("Producto escalar:", a * b)
print("Producto vectorial:", a.productoVectorial(b))