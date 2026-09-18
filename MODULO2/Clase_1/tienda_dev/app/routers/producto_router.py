from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi import HTTPException


from app.config.database import get_db
from app.schemas.producto_schemas import (
    ProductoCreate,
    ProductoUpdate,
    ProductoRespuesta,
)
from app.services import producto_service

router = APIRouter(prefix="/productos", tags=["Productos"])


@router.post("/", response_model=ProductoRespuesta)
def crear(datos: ProductoCreate, db: Session = Depends(get_db)):
    return producto_service.crear_producto(db, datos)


@router.get("/", response_model=list[ProductoRespuesta])
def listar(
    categoria_id: int | None = None,
    precio_max: float | None = None,
    db: Session = Depends(get_db),
):
    return producto_service.listar_productos(db, categoria_id, precio_max)


@router.get("/{producto_id}", response_model=ProductoRespuesta)
def obtener(producto_id: int, db: Session = Depends(get_db)):
    producto = producto_service.obtener_producto(db, producto_id)

    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return producto


@router.put("/{producto_id}", response_model=ProductoRespuesta)
def actualizar(
    producto_id: int,
    datos: ProductoCreate,
    db: Session = Depends(get_db),
):
    producto = producto_service.actualizar_producto(db, producto_id, datos)

    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return producto


@router.patch("/{producto_id}", response_model=ProductoRespuesta)
def actualizar_parcial(
    producto_id: int,
    datos: ProductoUpdate,
    db: Session = Depends(get_db),
):
    producto = producto_service.actualizar_parcial_producto(
        db,
        producto_id,
        datos,
    )

    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return producto



@router.put("/productos/{producto_id}", response_model=ProductoRespuesta)
def actualizar(producto_id: int, datos: ProductoCreate, db: Session = Depends(get_db)):
    producto = producto_service.actualizar_producto(db, producto_id, datos)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.delete("/productos/{producto_id}")
def eliminar(producto_id: int, db: Session = Depends(get_db)):
    eliminado = producto_service.eliminar_producto(db, producto_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": f"Producto {producto_id} eliminado"}



# from fastapi import APIRouter, HTTPException
# from app.schemas.producto_schemas import ProductoCreate, ProductoUpdate
# from app.services import producto_service

# router = APIRouter(prefix="/productos", tags=["Productos"])

# @router.post("/")
# def crear(producto: ProductoCreate):
#     nuevo = producto_service.crear_producto(producto)
#     return {"mensaje": "Producto creado exitosamente", "producto": nuevo}


# @router.get("/")
# def listar(categoria: str | None = None, precio_max: float | None = None):
#     resultado = producto_service.listar_productos(categoria, precio_max)
#     return {"total": len(resultado), "productos": resultado}

# @router.get("/{producto_id}")
# def obtener(producto_id: int):
#     producto = producto_service.obtener_producto(producto_id)
#     if producto is None:
#         raise HTTPException(status_code=404, detail="Producto no encontrado")
#     return producto


# @router.put("/{producto_id}")
# def actualizar(producto_id: int, datos: ProductoCreate):
#     producto = producto_service.actualizar_producto(producto_id, datos)
#     if producto is None:
#         raise HTTPException(status_code=404, detail="Producto no encontrado")
#     return {"mensaje": "Producto actualizado", "producto": producto}


# @router.delete("/{producto_id}")
# def eliminar(producto_id: int):
#     eliminado = producto_service.eliminar_producto(producto_id)
#     if not eliminado:
#         raise HTTPException(status_code=404, detail="Producto no encontrado")
#     return {"mensaje": f"Producto {producto_id} eliminado correctamente"}


# @router.patch("/{producto_id}")
# def actualizar_parcial(producto_id: int, datos: ProductoUpdate):
#     producto = producto_service.actualizar_parcial_producto(producto_id, datos)
#     if producto is None:
#         raise HTTPException(status_code=404, detail="Producto no encontrado")
#     return {"mensaje": "Producto actualizado parcialmente", "producto": producto}

