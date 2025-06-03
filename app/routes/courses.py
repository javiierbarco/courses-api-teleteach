from fastapi import APIRouter, HTTPException
from app.core.db import db
from app.models.course import Course, UserProgress, ProgressUpdate
from bson import ObjectId

router = APIRouter()

@router.get("/api/courses", response_model=list[Course])
async def get_courses():
    cursos = await db["courses"].find().to_list(length=100)
    for curso in cursos:
        curso["id"] = str(curso["_id"])
        del curso["_id"]
    return cursos

@router.get("/api/courses/{id}", response_model=Course)
async def get_course(id: str):
    curso = await db["courses"].find_one({"_id": ObjectId(id)})
    if curso:
        curso["id"] = str(curso["_id"])
        del curso["_id"]
        return curso
    raise HTTPException(status_code=404, detail="Curso no encontrado")

@router.post("/api/courses/{id}/progress")
async def registrar_progreso(id: str, progreso: ProgressUpdate):
    result = await db["progress"].insert_one({
        "course_id": id,
        "progress": progreso.dict()
    })
    return {"message": f"Progreso registrado para curso {id}", "id": str(result.inserted_id)}

@router.get("/api/courses/user/{user_id}/progress", response_model=UserProgress)
async def obtener_progreso_usuario(user_id: str):
    progreso = await db["user_progress"].find_one({"user_id": user_id})
    if progreso:
        progreso["id"] = str(progreso["_id"])
        del progreso["_id"]
        return progreso
    raise HTTPException(status_code=404, detail="Progreso no encontrado")
