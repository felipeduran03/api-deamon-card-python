from fastapi import APIRouter
from models.personaje import Personaje
from services.personaje_service import PersonajeService

router = APIRouter(
    prefix="/api-card-demonic/demonic/card",
    tags=["Personajes"]
)

@router.get("/random", response_model=Personaje)
def get_random_personaje():
    return PersonajeService.get_random()
