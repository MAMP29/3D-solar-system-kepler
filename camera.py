from ursina import *

class CustomCamera(Entity):
    def __init__(self):
        super().__init__()
        camera.parent = self
        self.rotation_speed = 5000  # Velocidad de rotación con el mouse
        self.zoom_speed = 2        # Velocidad de zoom
        self.zoom_min = 5          # Límite mínimo de zoom
        self.zoom_max = 500        # Límite máximo de zoom
        self.current_zoom = 50     # Valor inicial del zoom
        self.target_zoom = 20      # Para interpolación suave
        self.smooth_speed = 10     # Velocidad de interpolación

        # Bindings personalizados
        input_handler.bind('scroll up', 'zoom_in')
        input_handler.bind('scroll down', 'zoom_out')

    def update(self):
        # Rotación de la cámara con el mouse
        if held_keys['right mouse']:  # Mantener presionado botón derecho para rotar
            self.rotation_y += mouse.velocity[0] * self.rotation_speed * time.dt
            self.rotation_x -= mouse.velocity[1] * self.rotation_speed * time.dt
            
         # Interpolación suave del zoom
        if abs(self.current_zoom - self.target_zoom) > 0.01:
            self.current_zoom = lerp(self.current_zoom, self.target_zoom, time.dt * self.smooth_speed)
            camera.position = Vec3(0, 0, -self.current_zoom)

    def input(self, key):
        if key == 'zoom_in':
            self.target_zoom = max(self.zoom_min, self.target_zoom - self.zoom_speed)
        elif key == 'zoom_out':
            self.target_zoom = min(self.zoom_max, self.target_zoom + self.zoom_speed)
