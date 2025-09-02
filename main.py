from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from controllers.personaje_controller import router as personaje_router

app = FastAPI()

# 👇 Aquí está lo de CORS
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

# 👇 Servir imágenes estáticas
app.mount(
    "/static",
    StaticFiles(directory=r"C:\Users\luisf\OneDrive\Desktop\API 2\img"),
    name="static"
)


# ------------------------------
# 🔐 Seguridad con API Key
# ------------------------------
API_KEY = "1234"   # 👉 cámbiala por algo más seguro
API_KEY_NAME = "X-API-KEY"

async def api_key_auth(request: Request):
    api_key = request.headers.get(API_KEY_NAME)
    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API Key inválida o ausente",
            headers={"WWW-Authenticate": "API key"},
        )
    return True

# 👇 Registrar las rutas con seguridad
app.include_router(
    personaje_router,
    dependencies=[Depends(api_key_auth)]  # ✅ todas las rutas del router requieren X-API-Key
)