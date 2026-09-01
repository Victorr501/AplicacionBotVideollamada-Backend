from fastapi import FastAPI
from controllers import BotController

app = FastAPI(
      title="API Asistente de Reuniones"
    )

app.include_router(BotController.router)

