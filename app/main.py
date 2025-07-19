from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute
from dotenv import load_dotenv
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import os
import time
from starlette.responses import Response as StarletteResponse

from app.routes.courses import router as courses_router

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
app = FastAPI(
    title=os.getenv("API_NAME", "TeleTeach - API de Cursos"),
    description="API para gestión de cursos y seguimiento de progreso de usuarios docentes",
    version=os.getenv("API_VERSION", "0.1.0")
)

# === CORS ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
