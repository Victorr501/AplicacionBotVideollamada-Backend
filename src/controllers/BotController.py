from fastapi import APIRouter, Depends, Request
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