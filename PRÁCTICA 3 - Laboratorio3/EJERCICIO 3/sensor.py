class Sensor:
    tipo = "Generico"
    def __init__(self, id):
        self.id = id
        self.encendido = False
    def activar(self):
        self.encendido = True
    def desactivar(self):
        self.encendido = False
class Camara(Sensor):
    tipo = "Camara"
    def __init__(self, id, resolucion):
        super().__init__(id)
        self.resolucion = resolucion
class SensorLuzLaser(Sensor):
    tipo = "Luz Laser"
    def __init__(self, id, alcance):
        super().__init__(id)
        self.alcance = alcance
class VehiculoAutonomo(Camara, SensorLuzLaser):
    tipo = "Vehiculo Autonomo"
    def __init__(self, id, resolucion, alcance):
        Sensor.__init__(self, id)
        self.resolucion = resolucion
        self.alcance = alcance
v1 = VehiculoAutonomo(25, "4K", 250)

print("Tipo:", v1.tipo)
print("ID:", v1.id)
print("Resolucion:", v1.resolucion)
print("Alcance:", v1.alcance)
print("Encendido:", v1.encendido)

v1.activar()
print("Encendido:", v1.encendido)
v1.desactivar()
print("Encendido:", v1.encendido)