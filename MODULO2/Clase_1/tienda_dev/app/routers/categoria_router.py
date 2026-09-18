from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi import HTTPException


from app.config.database import get_db
from app.schemas.categoria_schemas import CategoriaCreate, CategoriaRespuesta
from app.services import categoria_services

router = APIRouter(prefix="/categorias", tags=["Categorías"])


@router.post("/", response_model=CategoriaRespuesta)
def crear(datos: CategoriaCreate, db: Session = Depends(get_db)):
    return categoria_services.crear_categoria(db, datos)


@router.get("/", response_model=list[CategoriaRespuesta])
def listar(db: Session = Depends(get_db)):
    return categoria_services.listar_categorias(db)


@router.get("/{categoria_id}", response_model=CategoriaRespuesta)
def obtener(categoria_id: int, db: Session = Depends(get_db)):
    categoria = categoria_services.obtener_categoria(db, categoria_id)

    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")

    return categoria



@router.put("/categorias/{categoria_id}", response_model=CategoriaRespuesta)
def actualizar(categoria_id: int, datos: CategoriaCreate, db: Session = Depends(get_db)):
    categoria = categoria_services.actualizar_categoria(db, categoria_id, datos)
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria


@router.delete("/categorias/{categoria_id}")
def eliminar(categoria_id: int, db: Session = Depends(get_db)):
    eliminado = categoria_services.eliminar_categoria(db, categoria_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return {"mensaje": f"Categoría {categoria_id} eliminada"}

# from fastapi import APIRouter, HTTPException
# from app.schemas.categoria_schemas import CategoriaCreate
# from app.services import categoria_services

# router = APIRouter(prefix="/categorias", tags=["Categorias"])


# @router.post("/")
# def crear(categoria: CategoriaCreate):
#     nueva = categoria_services.crear_categoria(categoria)
#     return {"mensaje": "Categoria creada exitosamente", "categoria": nueva}


# @router.get("/")
# def listar():
#     resultado = categoria_services.listar_categorias()
#     return {"total": len(resultado), "categorias": resultado}

# # @router.get("/{categoria_id}")
# # def obtener(categoria_id: int):
# #     categoria = categoria_services.obtener_categoria(categoria_id)
# #     if categoria is None:
# #         raise HTTPException(status_code=404, detail="Categoria no encontrada")
# #     return categoria

# @router.get("/categorias/{categoria_id}")
# def obtener(categoria_id: int):
#     return categoria_service.obtener_categoria(categoria_id)

# @router.put("/{categoria_id}")
# def actualizar(categoria_id: int, datos: CategoriaCreate):
#     categoria = categoria_services.actualizar_categoria(categoria_id, datos)
#     if categoria is None:
#         raise HTTPException(status_code=404, detail="Categoria no encontrada")
#     return {"mensaje": "Categoria actualizada", "categoria": categoria}


# @router.delete("/{categoria_id}")
# def eliminar(categoria_id: int):
#     eliminada = categoria_services.eliminar_categoria(categoria_id)
#     if not eliminada:
#         raise HTTPException(status_code=404, detail="Categoria no encontrada")
#     return {"mensaje": f"Categoria {categoria_id} eliminada correctamente"}