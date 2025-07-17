from app.db.mongo import db
from app.models.user_model import get_password_hash, verify_password

def generate_username(nombres: str, apellidos: str) -> str:
    base = (nombres[0] + apellidos).lower().replace(" ", "")
    username = base
    counter = 1
    while db.users.find_one({"username": username}):
        username = f"{base}{counter}"
        counter += 1
    return username

async def get_all_users():
    users_cursor = db.users.find()
    users = []
    async for user in users_cursor:
        users.append({
            "id": str(user["_id"]),
            "username": user["username"],
            "nombres": user["nombres"],
            "apellidos": user["apellidos"],
            "email": user["email"]
        })
    return users

async def create_user(user_data):
    username = generate_username(user_data.nombres, user_data.apellidos)
    hashed_password = get_password_hash(user_data.password)
    user_doc = {
        "username": username,
        "nombres": user_data.nombres,
        "apellidos": user_data.apellidos,
        "email": user_data.email,
        "password": hashed_password
    }
    result = await db.users.insert_one(user_doc)
    return {
        "id": str(result.inserted_id),
        "username": username,
        "nombres": user_data.nombres,
        "apellidos": user_data.apellidos,
        "email": user_data.email
    }

async def login_user(username: str, password: str):
    user = await db.users.find_one({"username": username})
    if user and verify_password(password, user["password"]):
        return {
            "id": str(user["_id"]),
            "username": user["username"],
            "nombres": user["nombres"],
            "apellidos": user["apellidos"],
            "email": user["email"]
        }
    return None
