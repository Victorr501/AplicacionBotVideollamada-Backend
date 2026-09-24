import logging
import sys
from pathlib import Path

Path("logs").mkdir(exist_ok=True)

FORMATO = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"

logging.basicConfig(
    level=logging.INFO, # Captura INFO, WARNING, ERROR y CRITICAL
    format=FORMATO,
    handlers=[
        logging.FileHandler("logs/app.log", encoding="utf-8"), # Guarda en disco
        logging.StreamHandler(sys.stdout)                      # Muestra en terminal
    ]
)