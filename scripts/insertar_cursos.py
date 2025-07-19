# Importa asyncio para ejecutar funciones asíncronas (requerido por motor)
import asyncio

# Importa el cliente asíncrono para MongoDB
from motor.motor_asyncio import AsyncIOMotorClient

# Importa load_dotenv para cargar variables de entorno desde el archivo .env
from dotenv import load_dotenv

# Importa el módulo os para acceder a las variables de entorno
import os

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Obtiene la URI de conexión desde las variables de entorno, o usa una por defecto
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")

# Obtiene el nombre de la base de datos, por defecto "teleteach"
DB_NAME = os.getenv("DB_NAME", "teleteach")

# Crea un cliente asíncrono para conectarse a MongoDB
client = AsyncIOMotorClient(MONGODB_URI)

# Obtiene una referencia a la base de datos
db = client[DB_NAME]

# Lista de cursos que se insertarán en la colección "courses"
cursos = [
    {
        "title": "Curso de Zoom",                    # Título del curso
        "description": "Aprende a usar Zoom para clases virtuales",  # Descripción
        "level": "básico"                            # Nivel del curso
    },
    {
        "title": "Curso de Meet",
        "description": "Domina Google Meet en tus clases",
        "level": "básico"
    }
]

# Función asíncrona para insertar los cursos en la base de datos
async def insertar_cursos():
    result = await db["courses"].insert_many(cursos)  # Inserta los documentos
    # Imprime los IDs generados por MongoDB para cada curso insertado
    print(f"Cursos insertados con IDs: {[str(id) for id in result.inserted_ids]}")

# Punto de entrada: ejecuta la función si el script se ejecuta directamente
if __name__ == "__main__":
    asyncio.run(insertar_cursos())
