from fastapi import APIRouter, Depends
from services.botServices.BotServices import BotServices
from services.botServices.IBotServices import IBotServices
from modelos.Reunion.ReunionInput import ReunionInputModel

router = APIRouter(prefix="/api/bot", tags=["Bot Reuniones"])

def get_bot_service() -> IBotServices:
    return BotServices()

@router.post("/unir")
def solicitar_bot(datos: ReunionInputModel, service: IBotServices = Depends(get_bot_service)):
    """
    Endpoint para solicitar que el bot se una a una reunión.
    """
    return service.enviar_bot(datos.url_reunion)

@router.post("/webhook")
def recibir_transcripcion(payload: dict, service: IBotServices = Depends(get_bot_service)):
    """
    Endpoint para recibir la transcripción de audio desde el bot.
    """
    return service.procesar_audio(payload)