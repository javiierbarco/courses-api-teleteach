import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "teleteach")

client = AsyncIOMotorClient(MONGODB_URI)
db = client[DB_NAME]

async def eliminar_duplicados():
    pipeline = [
        {
            "$group": {
                "_id": "$title",
                "ids": {"$push": "$_id"},
                "count": {"$sum": 1}
            }
        },
        {
            "$match": {
                "count": { "$gt": 1 }
            }
        }
    ]

    duplicados = await db["courses"].aggregate(pipeline).to_list(length=100)

    total_eliminados = 0

    for doc in duplicados:
        ids = doc["ids"]
        # Mantener el primero, eliminar los demás
        ids_a_eliminar = ids[1:]
        result = await db["courses"].delete_many({ "_id": { "$in": ids_a_eliminar } })
        total_eliminados += result.deleted_count

    print(f"✅ Cursos duplicados eliminados: {total_eliminados}")

if __name__ == "__main__":
    asyncio.run(eliminar_duplicados())
