from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from app.routes.courses import router as courses_router

# Cargar variables de entorno desde .env
load_dotenv()

# Crear la app FastAPI
app = FastAPI(
    title=os.getenv("API_NAME", "TeleTeach - API de Cursos"),
    description="API para gestión de cursos y seguimiento de progreso de usuarios docentes",
    version=os.getenv("API_VERSION", "0.1.0")
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(courses_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o ['http://localhost:5173']
    allow_methods=["*"],
    allow_headers=["*"],
)