from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from controllers.personaje_controller import router as personaje_router

from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

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
# 🔐 Seguridad con Basic Auth
# ------------------------------
security = HTTPBasic()

def auth(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "diablo")   # usuario válido
    correct_password = secrets.compare_digest(credentials.password, "123")    # contraseña válida
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


# 👇 Registrar las rutas con seguridad
app.include_router(
    personaje_router,
    dependencies=[Depends(auth)]  # ✅ todas las rutas del router requieren Basic Auth
)