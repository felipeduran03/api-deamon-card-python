from fastapi import APIRouter
from models.personaje import Personaje
from services.personaje_service import PersonajeService
from typing import List


router = APIRouter(
    prefix="/api-card-demonic/demonic/card",
    tags=["Personajes"]
)

@router.get("/random", response_model=List[Personaje])
def get_random_personajes():
    return PersonajeService.get_random_two()