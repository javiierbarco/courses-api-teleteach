# Se importa BaseModel desde Pydantic, que se utiliza para definir modelos de datos con validación automática
from pydantic import BaseModel

# Se importa List desde typing, que se usa para definir listas tipadas (por ejemplo, listas de objetos)
from typing import List

# Modelo que representa un curso dentro del sistema
class Course(BaseModel):
    id: str                    # Identificador único del curso (puede ser el ObjectId como string)
    title: str                 # Título del curso
    description: str           # Descripción del contenido del curso
    level: str = "básico"      # Nivel del curso, por defecto es "básico"

# Modelo que representa el progreso del usuario en un tema específico del curso
class ProgressUpdate(BaseModel):
    topic: str                 # Nombre o identificador del tema dentro del curso
    completed: bool            # Indica si el tema ha sido completado (True o False)

# Modelo que representa el progreso de un usuario en un curso completo
class UserProgress(BaseModel):
    user_id: str                               # Identificador del usuario
    course_id: str                             # Identificador del curso
    progress: List[ProgressUpdate]             # Lista de objetos ProgressUpdate, uno por cada tema del curso
