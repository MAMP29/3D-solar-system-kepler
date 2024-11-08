from ursina import Entity
from ursina import Vec3


G = 1# Constante de gravitación universal
M_SOLAR = 100 # Masa del sol en kilogramos

# Clase que representa un planeta
# El modelo es un atributo, pues hay algunos personalizados
class Planet(Entity):
    def __init__(self, nombre: str, masa: float, radio: float, posicion, velocidad, periodo: float, modelp, material):
        super().__init__(
            model=modelp,
            scale=radio,
            texture=material,
            position=posicion
        )
        self.nombre = nombre
        self.masa = masa
        self.radio = radio
        self.posicion = posicion # Vector de posición
        self.velocidad = velocidad.normalized() * 2  # Normalizamos y ajustamos la velocidad inicial
        self.periodo = periodo # Periodo orbital
        #self.entity = Entity(model=modelp, scale=radio, texture=material)

    # Para la representación de la posición y velocidad se considera las leyes del movimiento de Newton, basadas en la constante de gravitación
    # universal

    # Calcula la aceleración de un planeta hacia al sol, se basa en la distancia y la ley de gravitación universal
    def calcular_aceleracion(self, sol_posicion):
        # Distancia al sol
        distancia = self.posicion - sol_posicion
        r = distancia.length()
        if r < 0.1:  # Evitar divisiones por números muy pequeños
            return Vec3(0,0,0)
        
        # Aceleración por la ley de gravitación universal
        aceleracion = -G * M_SOLAR / r**2

        vector = Vec3(0,0,0)
        #print("NORMALIZED")
        #print(type(distancia.normalized()))

        return distancia.normalized() * aceleracion

    def actualizar_posicion(self, sol_posicion, dt):
        print(f"Posición actual: {self.posicion}")
        print(f"Velocidad actual: {self.velocidad}")
        
        # Calcular aceleración
        aceleracion = self.calcular_aceleracion(sol_posicion)
        print(f"Aceleración calculada: {aceleracion}")
        
        # Actualizar velocidad
        self.velocidad += aceleracion * dt
        #print("Velocidad:", self.velocidad)
        
        # Actualizar la posición
        self.posicion += self.velocidad * dt
        #print("Posición actualizada:", self.posicion)
        
        # Actualizar la entidad gráfica en Ursina
        self.position = self.posicion
