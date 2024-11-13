from turtle import position
from ursina import *
from planet import Planet
from simulatioui import SimulationUI
from camera import CustomCamera
import numpy as np
import math

app = Ursina()

sol = Entity(model= "sphere",  scale=0.2 * 8 * 2, texture = "textures/2k_sun.jpg")

# Textura -> https://www.solarsystemscope.com/textures/
# Datos -> https://astronoo.com/es/articulos/caracteristicas-de-los-planetas.html
        
mercurio = Planet(
    nombre="Mercurio",
    distancia_ua=0.39,
    periodo_orbital=87.97,
    excentricidad=0.2056,
    modelp='sphere',
    material="textures/2k_mercury",
    escala=0.58,
)

venus = Planet(
    nombre="Venus",
    distancia_ua=0.72,
    periodo_orbital=224.70,
    excentricidad=0.007,
    modelp='sphere',
    material='textures/2k_venus_surface.jpg',
    escala=1
)

tierra = Planet(
    nombre="Tierra",
    distancia_ua=1.0,
    periodo_orbital=365.25, # días
    excentricidad=0.0167,
    modelp="sphere",
    material="textures/earth albedo.jpg",
    escala=1.25,
)

marte = Planet(
    nombre="Marte",
    distancia_ua=1.52,
    periodo_orbital=687.00,
    excentricidad=0.0934,
    modelp='sphere',
    material='textures/2k_mars.jpg',
    escala=0.73
)

jupiter = Planet(
    nombre="Júpiter",
    distancia_ua=5.20,
    periodo_orbital=4332.62,
    excentricidad=0.0484,
    modelp='sphere',
    material='textures/jupitermap.jpg',
    escala=4
)

saturno = Planet(
    nombre="Saturno",
    distancia_ua=9.58,
    periodo_orbital=10759.22,
    excentricidad=0.0541,
    modelp='sphere',
    material='textures/2k_saturn.jpg',
    escala=3
)

urano = Planet(
    nombre="Urano",
    distancia_ua=19.18,
    periodo_orbital=30687.15,
    excentricidad=0.0444,
    modelp='sphere',
    material='textures/2k_uranus.jpg',
    escala=2.50
)

neptuno = Planet(
    nombre="Neptuno",
    distancia_ua=30.07,
    periodo_orbital=60190.03,
    excentricidad=0.0085,
    modelp='sphere',
    material='textures/2k_neptune.jpg',
    escala=2
)

panel_mercurio = SimulationUI(mercurio)
panel_venus = SimulationUI(venus)
panel_tierra = SimulationUI(tierra)
panel_marte = SimulationUI(marte)
panel_jupiter = SimulationUI(jupiter)
panel_saturno = SimulationUI(saturno)
panel_urano = SimulationUI(urano)

panel_mercurio.disable()
panel_venus.disable()
panel_tierra.disable()
panel_marte.disable()
panel_jupiter.disable()
panel_saturno.disable()
panel_urano.disable()

class Sky(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = 'textures/StarsMap_2500x1250.jpg',
            parent = scene,
            scale = 500,
            double_sided = True
        )


sku = Sky()
#EditorCamera()
custom_camera = CustomCamera()

speed = 15


def update():

    global speed

    dt = time.dt # Delta time en cada frame
    #sol.rotation_y += dt * 5

    # Actualizar posiciones
    for entidad in scene.entities:
        if isinstance(entidad, Planet):
            entidad.actualizar_posicion(sol.position, dt)

    # Movimiento libre de la cámara con WASD
    if held_keys['w']:
        custom_camera.position += custom_camera.forward * speed * dt
    if held_keys['s']:
        custom_camera.position -= custom_camera.forward * speed * dt
    if held_keys['a']:
        custom_camera.position -= custom_camera.right * speed * dt
    if held_keys['d']:
        custom_camera.position += custom_camera.right * speed * dt
    if held_keys['q']:
        custom_camera.position += custom_camera.up * speed * dt
    if held_keys['e']:
        custom_camera.position -= custom_camera.up * speed * dt
    if held_keys['shift']:
        custom_camera.position += custom_camera.forward * 40 * dt

    # SUAVIZAR VIAJAR HACIA EL CENTRO
    if held_keys['c']:
        custom_camera.position = sol.position

app.run()
