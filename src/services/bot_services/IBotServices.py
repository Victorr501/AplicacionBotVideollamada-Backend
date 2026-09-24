from abc import ABC, abstractmethod

class IBotServices(ABC):

    @abstractmethod
    def enviar_bot(self, url_reunion: str) -> dict:
        pass

    @abstractmethod
    def procesar_audio(self, audio_file: dict) -> dict:
        pass
 



