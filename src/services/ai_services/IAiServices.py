from abc import ABC, abstractmethod

class IAiServices(ABC):
    @abstractmethod
    def procesar_transcripcion(self, texto: str) => str:
        """
        Recibe el texto en bruto de la reunión y devuelve un resumen o análisis generado por la IA.
        """
        pass

