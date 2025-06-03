
# 📘 CHANGELOG – Courses API (TeleTeach)

Este archivo documenta de manera minuciosa todos los cambios relevantes realizados en el microservicio de gestión de cursos de **TeleTeach**. Se sigue la convención de versionado [SemVer](https://semver.org/lang/es/).

---

## [0.1.0] - 2025-06-01
### Agregado
- Estructura inicial del microservicio con FastAPI y MongoDB.
- Configuración de conexión a la base de datos MongoDB usando motor asíncrono.
- Modelo de datos `Course` definido con validaciones de Pydantic.
- Endpoints REST creados para:
  - Obtener todos los cursos (`GET /api/courses`).
  - Obtener curso por ID (`GET /api/courses/{id}`).
  - Crear un nuevo curso (`POST /api/courses`).
  - Actualizar un curso existente (`PUT /api/courses/{id}`).
  - Eliminar un curso (`DELETE /api/courses/{id}`).

### Cambiado
- Diseño estructural del microservicio con separación clara entre `routes`, `models` y `core`.

### Documentación
- README inicial detallando configuración, ejecución y uso.
- Documentación Swagger disponible en `/docs`.

---

## [0.1.1] - 2025-06-02
### Agregado
- Endpoint de progreso de usuario:
  - `POST /api/courses/{course_id}/progress`: Registra puntaje y correo asociado.
- Validación de campos requeridos para `user_id`, `score` y `completed`.
- Mecanismo básico para evitar registros incompletos o corruptos.

### Corregido
- Corrección en el uso de ID de MongoDB (`ObjectId`) para compatibilidad con el esquema de datos.
- Ajuste en las respuestas JSON para incluir siempre el campo `id` en lugar de `_id`.

---

## [0.1.2] - 2025-06-03
### Cambiado
- Se quitó código comentado y se reordenaron imports para mejorar legibilidad.
- Mejoras en el formato de error al no encontrar cursos.

### Documentación
- Se actualizó `README.md` con instrucciones de despliegue y nuevas rutas de evaluación.

---
