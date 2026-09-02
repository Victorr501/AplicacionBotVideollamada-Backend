from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import BotController

app = FastAPI(
      title="API Asistente de Reuniones"
    )

# CONFIGURACIÓN CORS
# Permite que el frontend pueda hacer solicitudes a la API desde un dominio diferente
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite solicitudes desde cualquier origen aqui tendremos que cambiarlo para el local y azure
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

# RUTAS

app.include_router(BotController.router)

