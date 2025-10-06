import httpx
from app.config import settings

async def obtener_usuario(user_id: int):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{settings.USUARIOS_SERVICE_URL}/{user_id}")
        r.raise_for_status()
        return r.json()

async def obtener_tutorias(user_id: int):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{settings.TUTORIAS_SERVICE_URL}/user/{user_id}")
        r.raise_for_status()
        return r.json()

async def obtener_materia(materia_id: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{settings.MATERIAS_SERVICE_URL}/{materia_id}")
        r.raise_for_status()
        return r.json()["materia"]  # la API de materias devuelve { materia: {...} }
