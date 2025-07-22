from fastapi import APIRouter, HTTPException                 # Importa enrutador de FastAPI y excepciones HTTP
from app.core.db import db                                  # Importa la conexión a la base de datos
from app.models.course import Course, UserProgress, ProgressUpdate  # Importa los modelos de datos
from app.models.course import CourseCreate  # Nuevo modelo para creación
from fastapi import Body
from bson import ObjectId                                   # Importa ObjectId para trabajar con IDs de MongoDB

router = APIRouter()  # Crea el enrutador para las rutas de cursos

@router.post("/api/courses")
async def create_course(course: CourseCreate = Body(...)):
    result = await db["courses"].insert_one(course.dict())
    return {
        "message": "Curso creado exitosamente",
        "id": str(result.inserted_id)
    }

# Ruta GET para obtener todos los cursos
@router.get("/api/courses", response_model=list[Course])
async def get_courses():
    cursos = await db["courses"].find().to_list(length=100)  # Consulta hasta 100 cursos
    for curso in cursos:
        curso["id"] = str(curso["_id"])  # Convierte ObjectId a string
        del curso["_id"]                 # Elimina el campo original para evitar errores con Pydantic
    return cursos

# Ruta GET para obtener un curso por su ID
@router.get("/api/courses/{id}", response_model=Course)
async def get_course(id: str):
    curso = await db["courses"].find_one({"_id": ObjectId(id)})  # Busca el curso por ID
    if curso:
        curso["id"] = str(curso["_id"])  # Convierte ObjectId a string
        del curso["_id"]                 # Elimina el campo original
        return curso
    raise HTTPException(status_code=404, detail="Curso no encontrado")  # Error si no se encuentra

# Ruta POST para registrar el progreso de un usuario en un tema del curso
@router.post("/api/courses/{id}/progress")
async def registrar_progreso(id: str, progreso: ProgressUpdate):
    result = await db["progress"].insert_one({        # Inserta el progreso en la colección
        "course_id": id,
        "progress": progreso.dict()
    })
    return {
        "message": f"Progreso registrado para curso {id}",
        "id": str(result.inserted_id)
    }

# Ruta GET para obtener el progreso de un usuario en un curso
@router.get("/api/courses/user/{user_id}/progress", response_model=UserProgress)
async def obtener_progreso_usuario(user_id: str):
    progreso = await db["user_progress"].find_one({"user_id": user_id})  # Busca progreso del usuario
    if progreso:
        progreso["id"] = str(progreso["_id"])  # Convierte ObjectId a string
        del progreso["_id"]                   # Elimina el campo original
        return progreso
    raise HTTPException(status_code=404, detail="Progreso no encontrado")

@router.delete("/api/courses/{id}")
async def delete_course(id: str):
    result = await db["courses"].delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"message": f"Curso con ID {id} eliminado"}
    raise HTTPException(status_code=404, detail="Curso no encontrado")

@router.delete("/api/progress/{progress_id}")
async def delete_progress(progress_id: str):
    result = await db["progress"].delete_one({"_id": ObjectId(progress_id)})
    if result.deleted_count == 1:
        return {"message": f"Progreso con ID {progress_id} eliminado"}
    raise HTTPException(status_code=404, detail="Progreso no encontrado")

@router.delete("/api/courses/user/{user_id}/progress")
async def delete_user_progress(user_id: str):
    result = await db["user_progress"].delete_one({"user_id": user_id})
    if result.deleted_count == 1:
        return {"message": f"Progreso de usuario {user_id} eliminado"}
    raise HTTPException(status_code=404, detail="Progreso del usuario no encontrado")


@router.route('/error')
def error():
    return "Algo falló", 500
