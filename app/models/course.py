from pydantic import BaseModel
from typing import List

class Course(BaseModel):
    id: str
    title: str
    description: str
    level: str = "básico"

class ProgressUpdate(BaseModel):
    topic: str
    completed: bool

class UserProgress(BaseModel):
    user_id: str
    course_id: str
    progress: List[ProgressUpdate]