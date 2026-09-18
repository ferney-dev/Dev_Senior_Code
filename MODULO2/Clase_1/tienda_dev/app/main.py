from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from app.config.database import Base, engine
from app.models import producto_model, categoria_model, proveedor_model
from app.exceptions import CategoriaNoEncontrada, ProveedorNoEncontrado
from app.routers import producto_router, categoria_router, proveedor_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tienda Dev API")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/index.html", encoding="utf-8") as f:
        return f.read()


@app.exception_handler(CategoriaNoEncontrada)
def manejar_categoria_no_encontrada(request: Request, exc: CategoriaNoEncontrada):
    return JSONResponse(
        status_code=404,
        content={
            "error": "recurso_no_encontrado",
            "detalle": str(exc)
        },
    )


@app.exception_handler(ProveedorNoEncontrado)
def manejar_proveedor_no_encontrado(request: Request, exc: ProveedorNoEncontrado):
    return JSONResponse(
        status_code=404,
        content={
            "error": "recurso_no_encontrado",
            "detalle": str(exc)
        },
    )


app.include_router(producto_router.router)
app.include_router(categoria_router.router)
app.include_router(proveedor_router.router)