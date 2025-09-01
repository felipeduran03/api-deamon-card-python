import random
from models.personaje import Personaje

datos = [
    Personaje(nombre="Demonikachu", rango="Demoniaco", fuerza=80, imagen="/static/Demonikachu.png"),
    Personaje(nombre="Peppadiablo", rango="Demonio",   fuerza=50, imagen="/static/Peppadiablo.png"),
    Personaje(nombre="Demonikitty", rango="Demonito",  fuerza=120, imagen="/static/Demonikitty.png"),
]

class PersonajeService:
    @staticmethod  # Usando el servicio directamente, sin crear objetos
    def get_random() -> Personaje:
        return random.choice(datos)
