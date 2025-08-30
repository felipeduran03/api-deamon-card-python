from fastapi import FastAPI
from pydantic import BaseModel
import random
from fastapi.staticfiles import StaticFiles


class Personaje(BaseModel):
    nombre: str
    rango: str
    fuerza: int
    imagen: str

datos = [
    Personaje(
        nombre="Demonikachu",
        rango="Demoniaco",
        fuerza=80,
        imagen="/static/Demonikachu.png"
    ),
    Personaje(
        nombre="Peppadiablo",
        rango="Demonio",
        fuerza=50,
        imagen="/static/Demonikitty.png"
    ),
    Personaje(
        nombre="Demonikitty",
        rango="Demonito",
        fuerza=120,
        imagen="/static/Peppadiablo.png"
    )
]

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=r"C:\Users\luisf\OneDrive\Desktop\API 2\img"),
    name="static"
)


@app.get("/api-card-demonic/demonic/card/random", response_model=Personaje)
def read_root():
    rango = len(datos)
    numero = random.randint(0, (rango-1))
    return datos[numero]

