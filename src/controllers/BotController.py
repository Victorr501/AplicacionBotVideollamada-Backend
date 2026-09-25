from fastapi import APIRouter, Depends, Request, HTTPException
from services.bot_services.BotServices import BotServices
from services.bot_services.IBotServices import IBotServices
from modelos.Reunion.ReunionInput import ReunionInputModel
import logging

router = APIRouter(prefix="/api/bot", tags=["Bot Reuniones"])
logger = logging.getLogger(__name__)

def get_bot_service() -> IBotServices:
    return BotServices()

@router.post("/unir")
def solicitar_bot(datos: ReunionInputModel, service: IBotServices = Depends(get_bot_service)):
    """
    Endpoint para solicitar que el bot se una a una reunión.
    """
    try:
        return service.enviar_bot(datos.url_reunion)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ConnectionError as e:
        raise HTTPException(status_code=502, detail=str(e))
    except Exception as e:
        logger.error(f"Error interno no controlado en /unir: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor. Por favor, inténtalo más tarde.")

# Hay que aplicar que el webhook funcione correctamente
@router.post("/webhook")
async def recibir_transcripcion(request: Request, service: IBotServices = Depends(get_bot_service)):
    """
    Endpoint para recibir la transcripción de audio desde el bot.
    """
    payload = await request.json()

    tipo_evento = payload.get("event", "evento_desconocido")

    print("\n" + "=" * 50)
    print(f"[WEBHOOK] Evento recibido: {tipo_evento}")
    print("=" * 50)
    print(payload) # Imprime todos los datos crudos para que los investiguemos
    print("="*50 + "\n")

    #return service.procesar_audio(payload)