# ⚡ Data Management & Ingestion API

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

API REST diseñada para la ingesta de datos en tiempo real y consulta de registros con documentación automática Swagger/OpenAPI.

---

### 🛠️ Características

* **Validación de Esquemas:** Integración de `Pydantic` para garantizar la calidad del dato de entrada.
* **Documentación Interactiva:** Swagger UI generado automáticamente.
* **Backend Escalable:** Listo para integración con bases de datos como PostgreSQL o SQLite.

---

### 🚀 Ejecución Local

```bash
pip install fastapi uvicorn pydantic
uvicorn main:app --reload
