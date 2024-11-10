from ursina import *
# Clase para manejar la GUI

class SimulationUI(Entity):
    def __init__(self, planet):
        super().__init__(
            parent=camera.ui,
            model='quad',
            color=color.white66,
            scale=(0.4,1.50),
            position=(-0.62,0.2)
        )

        self.planet = planet

        # Texto para mostrar el valor actual
        self.texto_velocidad = Text(
            parent=self,
            text='Velocidad: 1x',
            position=(-0.2,0.15),
            color=color.black90,
            scale=(3,1)
        )

        # Crear slider
        self.slider = Slider(
            parent=self,
            min=1,
            max=50,
            default=1,
            step=5,
            x=-0.45,
            y=0.08,
            text='',
            dynamic=True,
            scale=(1.8,1)
        )


        # Función que se llama cuando el slider cambia
        def on_slider_changed():
            self.planet.factor_velocidad = self.slider.value
            self.texto_velocidad.text = f'Velocidad: {int(self.slider.value)}x'
            
        self.slider.on_value_changed = on_slider_changed

