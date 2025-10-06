from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Servicio de Historial de Asesorías")
app.include_router(router)
