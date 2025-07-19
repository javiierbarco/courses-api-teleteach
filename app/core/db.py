# Se importa el cliente asíncrono de MongoDB desde la librería motor
from motor.motor_asyncio import AsyncIOMotorClient

# Se importa la función load_dotenv para cargar variables de entorno desde un archivo .env
from dotenv import load_dotenv

# Se importa el módulo os para acceder a las variables de entorno del sistema
import os

# Se cargan las variables definidas en el archivo .env al entorno actual
load_dotenv()

# Se obtiene la URI de conexión a MongoDB desde las variables de entorno
# Si no está definida, se utiliza una conexión local por defecto
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")

# Se obtiene el nombre de la base de datos desde las variables de entorno
# Si no está definida, se usa "teleteach" como valor por defecto
DB_NAME = os.getenv("DB_NAME", "teleteach")

# Se crea un cliente de MongoDB utilizando la URI especificada
# Este cliente permite hacer operaciones de forma asíncrona
client = AsyncIOMotorClient(MONGODB_URI)

# Se accede a la base de datos específica dentro del cliente
# Esta base de datos será utilizada para las operaciones CRUD
db = client[DB_NAME]
