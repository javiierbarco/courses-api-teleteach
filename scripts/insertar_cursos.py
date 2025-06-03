import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "teleteach")

client = AsyncIOMotorClient(MONGODB_URI)
db = client[DB_NAME]

cursos = [
    {
        "title": "Curso de Zoom",
        "description": "Aprende a usar Zoom para clases virtuales",
        "level": "básico"
    },
    {
        "title": "Curso de Meet",
        "description": "Domina Google Meet en tus clases",
        "level": "básico"
    }
]

async def insertar_cursos():
    result = await db["courses"].insert_many(cursos)
    print(f"Cursos insertados con IDs: {[str(id) for id in result.inserted_ids]}")

if __name__ == "__main__":
    asyncio.run(insertar_cursos())
