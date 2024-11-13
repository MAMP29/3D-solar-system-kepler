import math
from ursina import *
from ursina.prefabs.trail_renderer import TrailRenderer
from simulatioui import SimulationUI


# Constantes físicas
masa_sol = 1.989e30  # kg
G = 6.67430e-11     # m/s²
UA = 149597870700   # metros (1 Unidad Astronómica)

# Constantes de visualización
ESCALA_DISTANCIA = 10
ESCALA_TAMAÑO_BASE = 0.3
ESCALA_TIEMPO = 1e-5  # Factor para acelerar la simulación

# Clase que representa un planeta
# El modelo es un atributo, pues hay algunos personalizados
class Planet(Entity):
    def __init__(self, nombre: str, distancia_ua: float, periodo_orbital: float, excentricidad: float, modelp, material, escala: float = 1):
        

        # Convertir UA a metros para cálculos físicos
        self.semieje_mayor_real = distancia_ua * UA

        # Escala logaritmica
        distancia_visual = ESCALA_DISTANCIA * math.log(distancia_ua + 1)
        escala_ajustada = escala * ESCALA_TAMAÑO_BASE * (1 + math.log(escala + 0.1))

        super().__init__(
            model=modelp,
            scale=escala_ajustada,
            texture=material,
            collider='sphere'
        )

        self.nombre = nombre
        self.nombre = nombre
        self.factor_escala_visual = distancia_visual / distancia_ua
        self.semieje_mayor = distancia_visual
        self.excentricidad = excentricidad
        

        self.periodo = periodo_orbital * 86400
        
        # Calcular velocidad orbital
        self.velocidad_base = math.sqrt(G * masa_sol / self.semieje_mayor_real)
        
        self.angulo = 0
        self.factor_velocidad = 1
        self.panel_control = SimulationUI(self)
        self.panel_control.disable()
        self.on_click = self.toggle_panel
        
        # Calcular parámetros de la órbita
        self.parametro_orbital = self.semieje_mayor_real * (1 - self.excentricidad**2)

        # Lista para almacenar los puntos del rastro
        self.orbit_rastro_vertices = []

        self.max_rastro_puntos = 2000 * (distancia_ua / 1)

        self.linea_rastro = Entity(model=Mesh(mode='line', thickness=0.01), color=color.gray)

        #self.create()

    def toggle_panel(self):

        # Desactivar todos los otros paneles primero
        for entidad in scene.entities:
            if isinstance(entidad, Planet) and entidad != self:
                entidad.panel_control.disable()

        # Activar el panel de control del planeta
        if self.panel_control.enabled:
            self.panel_control.disable()
        else:
            self.panel_control.enable()

    # Actualiza la posición del planeta, seguimos un planteamiento basado en orbitas, donde el cálculo de posición es denotado por la orbita
    def actualizar_posicion(self, centro_pos: Vec3, dt: float):

        # Aplicar escala de tiempo para acelerar la simulación
        dt = dt * ESCALA_TIEMPO

        # Calcular radio real según Kepler
        radio_real = self.semieje_mayor_real * (1 - self.excentricidad * math.cos(self.angulo)) # r = a * (1 - e * cos(θ))
        
        # Calcular velocidad angular usando la segunda ley de Kepler
        # La velocidad angular varía inversamente con el cuadrado de la distancia
        velocidad_angular = (self.velocidad_base * 
                           math.sqrt(self.semieje_mayor_real * (1 + self.excentricidad) / 
                                   (radio_real * (1 - self.excentricidad)))) * self.factor_velocidad
        
        # Actualizar ángulo
        self.angulo += velocidad_angular * dt
        
        # Convertir radio real a visual
        radio_visual = (radio_real / UA) * self.factor_escala_visual
        
        # Calcular posición visual
        x = radio_visual * math.cos(self.angulo)
        z = radio_visual * math.sin(self.angulo)
        self.position = centro_pos + Vec3(x, 0, z)


        self.actualizar_rastro()

        # Rotación sobre el eje
        self.rotation_y += dt * 20

        # Información de debug
        if self.nombre == "Tierra":  # Solo mostrar debug para un planeta
            print(f"{self.nombre}:")
            print(f"Radio real (UA): {radio_real/UA:.2f}")
            print(f"Radio visual: {radio_visual:.2f}")
            print(f"Velocidad angular (rad/s): {velocidad_angular:.2e}")
            print(f"Velocidad orbital (km/s): {(velocidad_angular * radio_real)/1000:.2f}")
            print(f"posicion {self.position}")


    def actualizar_rastro(self):
        # Añadir la posición actual a los vértices
        self.orbit_rastro_vertices.append(self.position)

        # Limitar el rastro a un número máximo de puntos
        if len(self.orbit_rastro_vertices) > self.max_rastro_puntos:
            self.orbit_rastro_vertices.pop(0)  # Remover el punto más antiguo

        # Solo generar la línea si hay al menos dos puntos
        if len(self.orbit_rastro_vertices) >= 2:
            self.linea_rastro.model.vertices = self.orbit_rastro_vertices
            self.linea_rastro.model.generate()


