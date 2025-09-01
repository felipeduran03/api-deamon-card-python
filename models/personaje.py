from pydantic import BaseModel

class Personaje(BaseModel):
    nombre: str
    rango: str
    fuerza: int
    imagen: str
