# Importación de FastAPI para crear la aplicación web
from fastapi import FastAPI

# Importación del middleware de CORS para permitir conexiones desde otros dominios (como el frontend)
from fastapi.middleware.cors import CORSMiddleware

# Importación de dotenv para cargar variables de entorno desde un archivo .env
from dotenv import load_dotenv

# Módulo estándar para acceder a las variables de entorno
import os

# Importación del enrutador definido para el módulo de cursos
from app.routes.courses import router as courses_router

# Cargar variables de entorno desde el archivo .env al entorno del sistema
load_dotenv()

# Crear instancia de la aplicación FastAPI con metadatos opcionales
app = FastAPI(
    title=os.getenv("API_NAME", "TeleTeach - API de Cursos"),        # Nombre de la API desde .env o por defecto
    description="API para gestión de cursos y seguimiento de progreso de usuarios docentes",
    version=os.getenv("API_VERSION", "0.1.0")                        # Versión de la API desde .env o por defecto
)

# Configurar el middleware CORS para permitir peticiones desde frontend (React, etc.)
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "*").split(","),  # Permitir orígenes definidos en .env o todos (*)
    allow_credentials=True,      # Permitir el uso de cookies/autenticación en las peticiones
    allow_methods=["*"],         # Permitir todos los métodos HTTP (GET, POST, PUT, etc.)
    allow_headers=["*"],         # Permitir todos los encabezados
)

# Incluir las rutas del enrutador de cursos en la aplicación principal
app.include_router(courses_router)

# (OPCIONAL / REPETIDO) Segunda configuración de CORS (esto sobrescribe la anterior y no es necesario repetir)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],         # Esta línea permite todos los orígenes, útil en desarrollo
    allow_methods=["*"],
    allow_headers=["*"],
)
