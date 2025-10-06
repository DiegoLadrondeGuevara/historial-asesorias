from pydantic import BaseSettings

class Settings(BaseSettings):
    USUARIOS_SERVICE_URL: str
    TUTORIAS_SERVICE_URL: str
    MATERIAS_SERVICE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
