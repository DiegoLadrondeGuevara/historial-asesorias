from fastapi import APIRouter, HTTPException
from app.services import obtener_usuario, obtener_tutorias, obtener_materia

router = APIRouter()

@router.get("/historial-asesorias/{user_id}")
async def historial_asesorias(user_id: int):
    try:
        usuario = await obtener_usuario(user_id)
        tutorias = await obtener_tutorias(user_id)

        # Agregar info de materia a cada tutoría
        for tutoria in tutorias:
            materia_id = tutoria.get("materia_id")
            if materia_id:
                try:
                    materia_info = await obtener_materia(materia_id)
                    tutoria["materia_info"] = materia_info
                except Exception:
                    tutoria["materia_info"] = {"error": "No se pudo obtener información de la materia"}

        return {
            "usuario": usuario,
            "tutorias": tutorias
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener historial: {str(e)}")
