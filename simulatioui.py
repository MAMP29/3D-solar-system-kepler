from ursina import *
# Clase para manejar la GUI

class SimulationUI:
    def __init__(self):

        # Panel para el slider
        self.panel = Entity(
            parent=camera.ui,
            model='quad',
            color=color.white66,
            scale=(0.4,1.50),
            position=(-0.62,0.2)
        )

        # Texto para mostrar el valor actual
        self.text = Text(
            parent=self.panel,
            text='Velocidad: 1x',
            position=(-0.2,0.15),
            color=color.black90,
            scale=(3,1)
        )

        # Crear slider
        self.slider = Slider(
            parent=self.panel,
            min=1,
            max=50,
            default=1,
            step=4,
            x=-0.45,
            y=0.08,
            text='',
            dynamic=True,
            scale=(1.8,1)
        )

        # Factor de velocidad actual
        self.factor_velocidad = 1

        # Función que se llama cuando el slider cambia
        def on_slider_changed():
            self.factor_velocidad = self.slider.value
            self.text.text = f'Velocidad: {self.factor_velocidad}x'

        self.slider.on_value_changed = on_slider_changed

