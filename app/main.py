<<<<<<< HEAD
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute
from dotenv import load_dotenv
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
=======
# Importación de FastAPI para crear la aplicación web
from fastapi import FastAPI

# Importación del middleware de CORS para permitir conexiones desde otros dominios (como el frontend)
from fastapi.middleware.cors import CORSMiddleware

# Importación de dotenv para cargar variables de entorno desde un archivo .env
from dotenv import load_dotenv

# Módulo estándar para acceder a las variables de entorno
>>>>>>> 6859b74712d4a5b3a0a0fde55d292d840353df97
import os
import time
from starlette.responses import Response as StarletteResponse

# Importación del enrutador definido para el módulo de cursos
from app.routes.courses import router as courses_router

<<<<<<< HEAD
# === PROMETHEUS METRICS ===
REQUEST_COUNTER = Counter(
    "http_requests_total", "Total de peticiones HTTP", ["method", "endpoint"]
)
REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds", "Duración de peticiones HTTP", ["method", "endpoint"]
)
ERROR_COUNTER = Counter(
    "http_request_errors_total", "Errores HTTP por endpoint", ["method", "endpoint", "status"]
)

# === CARGA DE VARIABLES ===
load_dotenv()

# === CREACIÓN DE LA APP ===
=======
# Cargar variables de entorno desde el archivo .env al entorno del sistema
load_dotenv()

# Crear instancia de la aplicación FastAPI con metadatos opcionales
>>>>>>> 6859b74712d4a5b3a0a0fde55d292d840353df97
app = FastAPI(
    title=os.getenv("API_NAME", "TeleTeach - API de Cursos"),        # Nombre de la API desde .env o por defecto
    description="API para gestión de cursos y seguimiento de progreso de usuarios docentes",
    version=os.getenv("API_VERSION", "0.1.0")                        # Versión de la API desde .env o por defecto
)

<<<<<<< HEAD
# === CORS ===
=======
# Configurar el middleware CORS para permitir peticiones desde frontend (React, etc.)
>>>>>>> 6859b74712d4a5b3a0a0fde55d292d840353df97
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "*").split(","),  # Permitir orígenes definidos en .env o todos (*)
    allow_credentials=True,      # Permitir el uso de cookies/autenticación en las peticiones
    allow_methods=["*"],         # Permitir todos los métodos HTTP (GET, POST, PUT, etc.)
    allow_headers=["*"],         # Permitir todos los encabezados
)

<<<<<<< HEAD
# === INSTRUMENTACIÓN CON MIDDLEWARE ===
@app.middleware("http")
async def prometheus_metrics_middleware(request: Request, call_next):
    start_time = time.time()
    response: Response = await call_next(request)
    process_time = time.time() - start_time

    method = request.method
    endpoint = request.url.path
    status = response.status_code

    REQUEST_COUNTER.labels(method=method, endpoint=endpoint).inc()
    REQUEST_LATENCY.labels(method=method, endpoint=endpoint).observe(process_time)
    if status >= 400:
        ERROR_COUNTER.labels(method=method, endpoint=endpoint, status=str(status)).inc()

    return response

# === ENDPOINT PARA MÉTRICAS PROMETHEUS ===
@app.get("/metrics")
def metrics():
    return StarletteResponse(generate_latest(), media_type=CONTENT_TYPE_LATEST)

# === RUTAS ===
app.include_router(courses_router)
=======
# Incluir las rutas del enrutador de cursos en la aplicación principal
app.include_router(courses_router)

# (OPCIONAL / REPETIDO) Segunda configuración de CORS (esto sobrescribe la anterior y no es necesario repetir)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],         # Esta línea permite todos los orígenes, útil en desarrollo
    allow_methods=["*"],
    allow_headers=["*"],
)
>>>>>>> 6859b74712d4a5b3a0a0fde55d292d840353df97
