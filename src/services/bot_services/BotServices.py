from .IBotServices import IBotServices
from dotenv import load_dotenv
from config.http_client import http_client
import logging
import requests
import os

load_dotenv()
logging = logging.getLogger(__name__)

class BotServices(IBotServices):
    def __init__(self):
        self.api_key_bot = os.getenv("RECALL_API_KEY")
        self.url_proveedor = os.getenv("RECALL_API_URL")

    def enviar_bot(self, url_reunion: str) -> dict:
        logging.info(f"Conectando a bot a: {url_reunion}")

        if not self.api_key_bot:
            return {"status": "error", "message": "API key no configurada"}

        header = {
                "Authorization": f"Token {self.api_key_bot}",
            }

        payload = {
                "meeting_url": url_reunion,
                "bot_name": "Asistente de Reuniones IA"
            }

        try:
            respuesta = http_client.post(self.url_proveedor, data = payload, custom_headers = header)
            datos_bot = respuesta.json()

            return {
                    "status": "success",
                    "data": datos_bot.get("id"),
                    "recall_status": "joining",
                    "url_reunion": url_reunion
                }

        except requests.exceptions.RequestException as e:
            logging.error(f"Error: {e}")
            return {"status": "error", "message": "No se pudo conectar con el proveedor de bots."}

    def procesar_audio(self, audio_file: dict) -> dict:
        logging.info(f"Procesando archivo de audio...")
        return {"status": "ok", "transcription": "Texto transcrito del audio"}
 



