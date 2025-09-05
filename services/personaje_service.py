import random
from models.personaje import Personaje

datos = [
    Personaje(nombre="Demonikachu", rango="Demoniaco", fuerza=80, imagen="/static/Demonikachu.png"),
    Personaje(nombre="Peppadiablo", rango="Demonio",   fuerza=50, imagen="/static/Peppadiablo.png"),
    Personaje(nombre="Demonikitty", rango="Demonito",  fuerza=120, imagen="/static/Demonikitty.png"),
    Personaje(nombre="DoomBall", rango="Demonio",   fuerza=50, imagen="/static/DoomBall.png"),
    Personaje(nombre="Kael’thar", rango="Demonito",  fuerza=120, imagen="/static/Kaelthar.png"),
    Personaje(nombre="HellTubbie", rango="Demonito",  fuerza=120, imagen="/static/HellTubbie.png"),
    Personaje(nombre="Teemonio", rango="Demoniaco",  fuerza=120, imagen="/static/Teemonio.png"),
    Personaje(nombre="Infergar", rango="Demoniaco",  fuerza=120, imagen="/static/Infergar.png"),
    Personaje(nombre="Demonipreer", rango="Demonio",  fuerza=120, imagen="/static/Demonipreer.png"),
]

class PersonajeService:
    @staticmethod  # Usando el servicio directamente, sin crear objetos
    def get_random() -> Personaje:
        return random.choice(datos)

    @staticmethod
    def get_random_two() -> list[Personaje]:
        return random.sample(datos, 2)  # ← Devuelve 2 distintos