# 🐱 CatAPI Backend

Este proyecto es una API REST construida con **FastAPI**, conectada a **MongoDB**, con endpoints para usuarios, gatos y razas provenientes de [TheCatAPI](https://thecatapi.com/). Incluye autenticación, pruebas automatizadas y Docker.

---

## 🚀 Características

- Registro y login de usuarios
- Encriptación de contraseñas (bcrypt)
- Consulta de razas desde TheCatAPI
- Pruebas con `pytest`, `httpx` y `LifespanManager`
- Contenedores con Docker y Docker Compose
- Variables de entorno con `.env`

---

## 🛠️ Tecnologías

- Python 3.10
- FastAPI
- MongoDB (Motor)
- TheCatAPI
- Pytest + LifespanManager
- Docker
- Pydantic
- Passlib

---

## 🐳 Instalación con Docker

```bash
docker-compose up --build
