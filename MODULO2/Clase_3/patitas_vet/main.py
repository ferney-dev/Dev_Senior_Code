from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.config.database import Base, engine
from app.models import (
    dueno_model,
    mascota_model,
    veterinario_model,
    cita_model,
    insumo_model,
    tratamiento_model,
    tratamiento_insumo_model,
)
from app.routers import (
    aplicacion_router,
    cita_router,
    consultas_router,
    dueno_router,
    insumo_router,
    mascota_router,
    tratamiento_insumo_router,
    tratamiento_router,
    veterinario_router,
)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Patitas Vet API")

app.include_router(dueno_router.router)
app.include_router(mascota_router.router)
app.include_router(veterinario_router.router)
app.include_router(insumo_router.router)
app.include_router(cita_router.router)
app.include_router(tratamiento_router.router)
app.include_router(tratamiento_insumo_router.router)
app.include_router(aplicacion_router.router)
app.include_router(consultas_router.router)

# Montar archivos estáticos para la vista HTML (sirve static/index.html)
app.mount("/", StaticFiles(directory="static", html=True), name="static")