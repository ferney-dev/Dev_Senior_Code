from fastapi import FastAPI
from app.database import Base, engine
from app.models import usuario_model, medico_model, horario_model, cita_model
from app.routers import auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="MediReserva API")

app.include_router(auth_router.router)

@app.get("/")
def raiz():
    return {"mensaje": "MediReserva API funcionando"}