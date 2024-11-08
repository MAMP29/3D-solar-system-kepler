from turtle import position
from ursina import *
from planet import Planet
import numpy as np
import math

app = Ursina()

sol = Entity(model= "sphere",  scale=2, texture = "textures/2k_sun.jpg")
tierra = Planet(
    nombre="Tierra", 
    masa=1,  
    radio=1, 
    posicion=Vec3(10, 0, 0), 
    velocidad=Vec3(0, 0, 2), 
    periodo=365, 
    modelp="sphere", 
    material="textures/earth albedo.jpg")

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
    tierra.actualizar_posicion(sol.position, dt)




app.run()
