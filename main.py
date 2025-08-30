from fastapi import FastAPI
from pydantic import BaseModel
import random
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


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

origins = [
    "http://193.186.4.216:5500", 
    "http://127.0.0.1:5500",    # frontend local
    "https://midominio.com",   # dominio en producción
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

