from fastapi import FastAPI, Path, Body
from pydantic import BaseModel
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="TeleTeach - API de Cursos",
    description="API para gestión de cursos y seguimiento de progreso de usuarios docentes",
    version="0.1.0"
)

# Permitir CORS para desarrollo local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# MODELOS ----------------------------------------------

class Course(BaseModel):
    id: int
    title: str
    description: str
    level: Optional[str] = "básico"

class ProgressUpdate(BaseModel):
    topic: str
    completed: bool

class UserProgress(BaseModel):
    user_id: str
    course_id: int
    progress: List[ProgressUpdate]

# RUTAS ------------------------------------------------

@app.get("/api/courses/", response_model=List[Course])
def listar_cursos():
    return [
        {"id": 1, "title": "Curso de Zoom", "description": "Aprende a usar Zoom para clases virtuales"},
        {"id": 2, "title": "Curso de Meet", "description": "Domina Google Meet en tus clases"},
    ]

@app.get("/api/courses/{id}", response_model=Course)
def detalle_curso(id: int = Path(..., description="ID del curso a consultar")):
    return {"id": id, "title": "Curso de ejemplo", "description": "Contenido del curso de ejemplo"}

@app.post("/api/courses/{id}/progress")
def registrar_progreso(id: int, progreso: ProgressUpdate):
    return {"message": f"Progreso registrado para curso {id}", "progreso": progreso}

@app.get("/api/courses/user/{user_id}/progress", response_model=UserProgress)
def obtener_progreso_usuario(user_id: str):
    return {
        "user_id": user_id,
        "course_id": 1,
        "progress": [
            {"topic": "Introducción", "completed": True},
            {"topic": "Herramientas básicas", "completed": False}
        ]
    }
