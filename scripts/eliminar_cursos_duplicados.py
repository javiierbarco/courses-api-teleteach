# Importa asyncio para ejecutar funciones asíncronas de forma manual
import asyncio

# Importa el cliente asíncrono de MongoDB usando motor
from motor.motor_asyncio import AsyncIOMotorClient

# Importa load_dotenv para cargar variables de entorno desde un archivo .env
from dotenv import load_dotenv

# Importa el módulo os para acceder a variables de entorno
import os

# Carga las variables de entorno definidas en el archivo .env
load_dotenv()

# Obtiene la URI de conexión a MongoDB, con valor por defecto en caso de no existir
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")

# Obtiene el nombre de la base de datos, por defecto 'teleteach'
DB_NAME = os.getenv("DB_NAME", "teleteach")

# Crea el cliente de conexión a MongoDB
client = AsyncIOMotorClient(MONGODB_URI)

# Obtiene la base de datos específica
db = client[DB_NAME]

# Función asíncrona para eliminar cursos duplicados (por título)
async def eliminar_duplicados():
    # Pipeline de agregación: agrupa documentos con el mismo título
    pipeline = [
        {
            "$group": {
                "_id": "$title",                 # Agrupar por título
                "ids": {"$push": "$_id"},        # Guardar todos los _id con ese título
                "count": {"$sum": 1}             # Contar cuántos documentos hay por título
            }
        },
        {
            "$match": {
                "count": { "$gt": 1 }            # Filtrar solo los que tienen más de 1 (duplicados)
            }
        }
    ]

    # Ejecuta la agregación y convierte el resultado a lista
    duplicados = await db["courses"].aggregate(pipeline).to_list(length=100)

    total_eliminados = 0  # Contador de eliminados

    for doc in duplicados:
        ids = doc["ids"]
        # Mantiene solo el primer documento y elimina el resto
        ids_a_eliminar = ids[1:]
        result = await db["courses"].delete_many({ "_id": { "$in": ids_a_eliminar } })
        total_eliminados += result.deleted_count

    print(f"✅ Cursos duplicados eliminados: {total_eliminados}")

# Punto de entrada del script, ejecuta la función eliminar_duplicados si se ejecuta directamente
if __name__ == "__main__":
    asyncio.run(eliminar_duplicados())
