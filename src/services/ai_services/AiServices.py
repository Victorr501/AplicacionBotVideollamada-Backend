import logging
import os
import google.generativeai as genai
from .IAiServices import IAiServices

logger = logging.getLogger(__name__)

# Falta sustituir los print por logger

class AiServices(IAiServices):
    def __init__(self):
        # Cogemos tu clave del archivo .env
        api_key = os.getenv("GEMINI_API_KEY")
        
        if not api_key:
            print("[ADVERTENCIA] No se encontró GEMINI_API_KEY en el entorno.")
            
        # Configuramos la librería oficial de Google
        genai.configure(api_key=api_key)
        
        # Instanciamos el modelo. 'gemini-1.5-flash' es súper rápido y perfecto para procesar texto largo
        self.modelo = genai.GenerativeModel('gemini-1.5-flash')

    def procesar_transcripcion(self, texto: str) -> str:
        if not texto:
            return "No se ha proporcionado texto para procesar."
            
        # Aquí puedes ajustar el "prompt" para pedirle a la IA exactamente lo que quieras
        prompt = f"Actúa como un asistente ejecutivo. Haz un resumen estructurado con los puntos clave y tareas pendientes de esta reunión:\n\n{texto}"
        
        try:
            print("[IA] Enviando transcripción a Gemini...")
            respuesta = self.modelo.generate_content(prompt)
            return respuesta.text
            
        except Exception as e:
            print(f"[ERROR GEMINI] {e}")
            return "Hubo un error al procesar el texto con la IA."