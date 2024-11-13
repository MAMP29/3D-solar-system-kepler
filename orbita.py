from ursina import *
import math

from ursina import *

class Orbita(Entity):
    def __init__(self, semieje_mayor, excentricidad, centro=Vec3(0, 0, 0), color=color.white, segmentos=100):
        super().__init__()
        self.semieje_mayor = semieje_mayor
        self.excentricidad = excentricidad
        self.centro = centro
        self.color = color
        self.segmentos = segmentos
        
        self.generar_puntos()
        self.crear_modelo()
        
        self.disable()

    def generar_puntos(self):
        self.puntos = []
        for i in range(self.segmentos + 1):
            theta = i * (2 * math.pi / self.segmentos)
            r = self.semieje_mayor * (1 - self.excentricidad**2) / (1 + self.excentricidad * math.cos(theta))
            x = r * math.cos(theta)
            z = r * math.sin(theta)
            self.puntos.append(Vec3(x, 0, z) + self.centro)

    def crear_modelo(self):
        self.model = Mesh(vertices=self.puntos, mode='line', thickness=2)
        self.set_color(self.color)

    def mostrar(self):
        self.enable()

    def ocultar(self):
        self.disable()
        
    def set_color(self, color):
        self.color = color