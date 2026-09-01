from .IBotServices import IBotServices

class BotServices(IBotServices):
    def enviar_bot(self, url_reunion: str) -> dict:
        print(f"[SERVICIO] Conectando a bot a: {url_reunion}")
        return {"status": "ok", "url": url_reunion, "bot_id": "bot_xyz"}

    def procesar_audio(self, audio_file: dict) -> dict:
        print(f"[SERVICIO] Procesando archivo de audio...")
        return {"status": "ok", "transcription": "Texto transcrito del audio"}
 



