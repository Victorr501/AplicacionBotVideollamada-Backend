import logging
import os
import google.generativeai as genai
from .IAiServices import IAiServices

logger = logging.getLogger(__name__)

# Falta sustituir los print por logger

class AiServices(IAiServices):
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        
        if not api_key:
            logger.warning("[ADVERTENCIA] No se encontró GEMINI_API_KEY en el entorno.")
            
        genai.configure(api_key=api_key)
        
        # Instanciamos el modelo. 'gemini-1.5-flash' es súper rápido y perfecto para procesar texto largo
        self.modelo = genai.GenerativeModel('gemini-1.5-flash')

    def procesar_transcripcion(self, texto: str) -> str:
        if not texto:
            return "No se ha proporcionado texto para procesar."
            
        # Aquí puedes ajustar el "prompt" para pedirle a la IA exactamente lo que quieras
        prompt = f"Actúa como un asistente ejecutivo. Haz un resumen estructurado con los puntos clave y tareas pendientes de esta reunión:\n\n{texto}"
        
        try:
            logger.info("Enviando transcripción a Gemini...")
            respuesta = self.modelo.generate_content(prompt)
            return respuesta.text
            
        except Exception as e:
            logger.error(f"Error al conectar con Gemini: {e}")
            return "Hubo un error al procesar el texto con la IA."