import math
from ursina import Entity
from ursina import Vec3


G = 1# Constante de gravitación universal
M_SOLAR = 100 # Masa del sol en kilogramos

# Clase que representa un planeta
# El modelo es un atributo, pues hay algunos personalizados
class Planet(Entity):
    def __init__(self, nombre: str, distancia_ua: float, periodo_orbital: float, excentricidad: float, modelp, material, escala: float = 1):
        super().__init__(
            model=modelp,
            scale=escala,
            texture=material
        )

        # Para convertir unidades astronómicas a unidades de visualización para nuestro entorno
        ESCALA_DISTANCIA = 20 # 20 unidades = 1 UA (unidades astronómicas)

        self.nombre = nombre
        self.semieje_mayor = distancia_ua * ESCALA_DISTANCIA # Representar distancias proporcionales a las escalas establecidas
        self.excentricidad = excentricidad

        # La velocidad angular varía según la posición en la órbita
        # Período en días convertido a nuestra escala de tiempo
        self.periodo = periodo_orbital
        self.velocidad_base = (2 * math.pi) / periodo_orbital# Usado para determinar la velocidad angular promedio del objeto

        self.angulo = 0


    # Actualiza la posición del planeta, seguimos un planteamiento basado en orbitas, donde el cálculo de posición es denotado por la orbita
    def actualizar_posicion(self, centro_pos: Vec3, dt: float, factor_velocidad: float):
        # Calcular velocidad angular instantánea según la segunda ley de Kepler
        radio_actual = self.semieje_mayor * (1 - self.excentricidad * math.cos(self.angulo))
        velocidad_angular = self.velocidad_base * (self.semieje_mayor / radio_actual)**2 * factor_velocidad # Factor de velocidad para ajustar la velocidad

        # Actualizar ángulo con velocidad variable
        self.angulo += velocidad_angular * dt
        
        # Conversión de corrdenadas polares a cartesianas
        x = math.cos(self.angulo) * radio_actual
        z = math.sin(self.angulo) * radio_actual
        
        self.position = centro_pos + Vec3(x, 0, z)
        self.rotation_y += dt * 20 # Agrega rotación al planeta para simular su rotación sobre su propio eje

        # Debug info
        print(f"{self.nombre}:")
        print(f"Radio actual (UA): {radio_actual/20:.2f}")
        print(f"Velocidad angular: {velocidad_angular:.2f}")

