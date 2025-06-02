# 📚 TeleTeach – API de Cursos y Progreso

Este repositorio contiene el microservicio responsable de la gestión de cursos, visualización de contenido y seguimiento del progreso del usuario dentro del sistema **TeleTeach**.

Forma parte del desarrollo del curso **Ingeniería de Software 2 – 2025-1** y está basado en una arquitectura SOFEA.

---

## 🚀 Tecnologías utilizadas

- Python 3.11+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- Mock DB (diccionarios en memoria o archivo JSON para el MVP)

---

## ⚙️ Instalación y ejecución local

```bash
# Clona el repositorio
git clone https://github.com/javiierbarco/courses-api-teleteach.git
cd courses-api-teleteach

# Crea un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: .\venv\Scripts\activate

# Instala dependencias
pip install -r requirements.txt

# Ejecuta el servidor
uvicorn main:app --reload --port 8001
```

---

## 📋 Endpoints principales

| Método | Ruta                                       | Función                                  |
|--------|--------------------------------------------|-------------------------------------------|
| GET    | `/api/courses/`                            | Listar todos los cursos disponibles       |
| GET    | `/api/courses/{id}`                        | Obtener detalles de un curso              |
| POST   | `/api/courses/{id}/progress`               | Registrar progreso del usuario en curso   |
| GET    | `/api/courses/user/{user_id}/progress`     | Ver progreso acumulado del usuario        |

Puedes explorar la documentación Swagger en:

```
http://localhost:8001/docs
```

---

## 🔗 Otros Repositorios del Proyecto TeleTeach

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

---

## 📜 Licencia

Uso académico – Universidad Nacional de Colombia – Ingeniería de Sistemas y Computación – 2025-1
