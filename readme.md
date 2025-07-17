# 🐱 CatAPI Backend

Este proyecto es una API REST construida con **FastAPI**, conectada a **MongoDB**, con endpoints para usuarios, gatos y razas provenientes de [TheCatAPI](https://thecatapi.com/). Incluye autenticación, pruebas automatizadas y Docker.

## 🚀 Características

- Registro y login de usuarios
- Encriptación de contraseñas (bcrypt)
- Consulta de razas desde TheCatAPI
- Pruebas con `pytest` y `httpx`
- Contenedores con Docker y Docker Compose
- Variables de entorno con `.env`

## 🛠️ Tecnologías

- Python 3.10
- FastAPI
- MongoDB (con Motor)
- TheCatAPI
- Pytest + LifespanManager
- Docker
- Pydantic
- Passlib

## 🐳 Instalación con Docker

```bash
docker-compose up --build

🔐 Variables de entorno

Crea un archivo .env:

MONGO_URI=mongodb://mongo:27017
DB_NAME=catapi_db
THECATAPI_KEY=tu_api_key
SECRET_KEY=clave_secreta
ALGORITHM=HS256

📬 Endpoints destacados
POST /user → Crear usuario
POST /login → Login
GET /breeds/ → Obtener todas las razas
GET /breeds/search/?q=sib → Buscar razas