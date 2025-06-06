# 📘 TeleTeach – API de Cursos y Progreso

Este repositorio contiene el microservicio `courses-api-teleteach`, responsable de gestionar los cursos disponibles en la plataforma **TeleTeach** y registrar el progreso individual de los usuarios.

Forma parte del proyecto **TeleTeach**, desarrollado como parte del curso _Ingeniería de Software 2 – 2025-1_, bajo una arquitectura tipo SOFEA (Start-end Only Front-End Architecture).

---

## 🚀 Tecnologías utilizadas

- Python 3.11+
- FastAPI
- Uvicorn
- MongoDB (conexión vía `motor`)
- Pydantic para validación
- Dotenv para configuración por entorno

---

## ⚙️ Instalación y ejecución local

```bash
# Clona el repositorio
git clone https://github.com/javiierbarco/courses-api-teleteach.git
cd courses-api-teleteach

# En Linux/macOS: Crear un entorno virtual
python -m venv venv
source venv/bin/activate

# En Windows: Crear un entorno virtual
python -m venv venv
venv\Scripts\activate

# Instala las dependencias
pip install -r requirements.txt

# Crea el archivo .env si no existe
cp .env.example .env

# Ejecuta el servidor
uvicorn app.main:app --reload --port 8001
```

---

## 📦 Estructura del Proyecto

```
courses-api-teleteach/
├── app/
│   ├── main.py              # Configuración principal y arranque del servidor
│   ├── core/
│   │   └── db.py            # Conexión a MongoDB
│   ├── models/
│   │   └── course.py        # Modelos de datos con Pydantic
│   ├── routes/
│   │   └── courses.py       # Endpoints relacionados con cursos y progreso
├── .env.example             # Plantilla de configuración
├── requirements.txt         # Dependencias del proyecto
└── README.md                # Este archivo
```

---

## 📋 Endpoints principales

| Método | Ruta                               | Funcionalidad                           |
|--------|------------------------------------|------------------------------------------|
| GET    | `/api/courses`                     | Listar todos los cursos disponibles      |
| GET    | `/api/courses/{course_id}`         | Obtener detalle de un curso             |
| POST   | `/api/courses/{course_id}/progress`| Registrar progreso (correo, score, etc) |

Documentación Swagger disponible en:
```
http://localhost:8001/docs
```

---

## 📂 Variables de entorno (.env)

```env
MONGO_URL=mongodb://localhost:27017
MONGO_DB=teleteach
API_NAME=TeleTeach - API de Cursos
API_VERSION=0.1.0
ALLOWED_ORIGINS=http://localhost:5173
```

---

## 🔗 Repositorios relacionados

- [Frontend TeleTeach](https://github.com/javiierbarco/frontend-teleteach)
- [API de Autenticación](https://github.com/javiierbarco/auth-api-teleteach)

---

## 👥 Equipo Castores – Ingeniería de Software 2

- Diego H. Lavado G.  
- Estephanie Perez M.  
- Frank S. Pardo A.  
- Javier E. González V.  
- Juan D. Rivera B.  
- Victor M. Torres A.  
- Wullfredo J. Barco G.