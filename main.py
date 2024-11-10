from turtle import position
from ursina import *
from planet import Planet
from simulatioui import SimulationUI
import numpy as np
import math

app = Ursina()
ui = SimulationUI()

sol = Entity(model= "sphere",  scale=2, texture = "textures/2k_sun.jpg")
tierra = Planet(
    nombre="Tierra",
    distancia_ua=1.0,
    periodo_orbital=365.25, # días
    excentricidad=0.0167,
    modelp="sphere",
    material="textures/earth albedo.jpg",
    escala=1,
)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = 'textures/StarsMap_2500x1250.jpg',
            parent = scene,
            scale = 150,
            double_sided = True
        )


sku = Sky()
EditorCamera()

def update():
    dt = time.dt # Delta time en cada frame
    #sol.rotation_y += dt * 5
    tierra.actualizar_posicion(sol.position, dt, ui.factor_velocidad)




app.run()
