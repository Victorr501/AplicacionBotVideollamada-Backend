from .IBotServices import IBotServices
from dotenv import load_dotenv
import requests
import os

load_dotenv()

class BotServices(IBotServices):
    def __init__(self):
        self.api_key_bot = os.getenv("RECALL_API_KEY")
        self.url_proveedor = "https://eu-central-1.recall.ai/api/v1/bot/";

    def enviar_bot(self, url_reunion: str) -> dict:
        print(f"[SERVICIO] Conectando a bot a: {url_reunion}")

        if not self.api_key_bot:
            return {"status": "error", "message": "API key no configurada"}

        header = {
                "Authorization": f"Token {self.api_key_bot}",
                "Content-Type":"application/json" 
            }

        payload = {
                "meeting_url": url_reunion,
                "bot_name": "Asistente de Reuniones IA"
            }

        try:
            respuesta = requests.post(self.url_proveedor, headers=header, json=payload)

            respuesta.raise_for_status()

            datos_bot = respuesta.json()

            return {
                    "status": "success",
                    "data": datos_bot.get("id"),
                    "recall_status": "joining",
                    "url_reunion": url_reunion
                }

        except requests.exceptions.RequestException as e:
            print(f"[ERROR API RECALL] {e}")
            return {"status": "error", "message": "No se pudo conectar con el proveedor de bots."}

    def procesar_audio(self, audio_file: dict) -> dict:
        print(f"[SERVICIO] Procesando archivo de audio...")
        return {"status": "ok", "transcription": "Texto transcrito del audio"}
 



