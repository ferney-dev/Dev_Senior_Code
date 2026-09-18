
from sqlalchemy.orm import Session
from app.models.producto_model import Producto
from app.schemas.producto_schemas import ProductoCreate
from app.models.categoria_model import Categoria
from app.models.proveedor_model import Proveedor
from app.exceptions import CategoriaNoEncontrada, ProveedorNoEncontrado


def crear_producto(db: Session, datos: ProductoCreate):
    categoria = db.query(Categoria).filter(Categoria.id == datos.categoria_id).first()
    if categoria is None:
        raise CategoriaNoEncontrada(datos.categoria_id)

    if datos.proveedor_id is not None:
        proveedor = db.query(Proveedor).filter(Proveedor.id == datos.proveedor_id).first()
        if proveedor is None:
            raise ProveedorNoEncontrado(datos.proveedor_id)

    nuevo = Producto(
        nombre=datos.nombre,
        precio=datos.precio,
        stock=datos.stock,
        categoria_id=datos.categoria_id,
        proveedor_id=datos.proveedor_id,
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo



def listar_productos(db: Session, categoria_id=None, precio_max=None):
    consulta = db.query(Producto)

    if categoria_id is not None:
        consulta = consulta.filter(Producto.categoria_id == categoria_id)

    if precio_max is not None:
        consulta = consulta.filter(Producto.precio <= precio_max)

    return consulta.all()


def obtener_producto(db: Session, producto_id: int):
    return (
        db.query(Producto)
        .filter(Producto.id == producto_id)
        .first()
    )


def actualizar_producto(db: Session, producto_id: int, datos: ProductoCreate):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if producto is None:
        return None

    categoria = db.query(Categoria).filter(Categoria.id == datos.categoria_id).first()
    if categoria is None:
        raise CategoriaNoEncontrada(datos.categoria_id)

    if datos.proveedor_id is not None:
        proveedor = db.query(Proveedor).filter(Proveedor.id == datos.proveedor_id).first()
        if proveedor is None:
            raise ProveedorNoEncontrado(datos.proveedor_id)

    producto.nombre = datos.nombre
    producto.precio = datos.precio
    producto.stock = datos.stock
    producto.categoria_id = datos.categoria_id
    producto.proveedor_id = datos.proveedor_id
    db.commit()
    db.refresh(producto)
    return producto


def actualizar_parcial_producto(db: Session, producto_id: int, datos):
    producto = obtener_producto(db, producto_id)

    if not producto:
        return None

    cambios = datos.model_dump(exclude_unset=True)

    for campo, valor in cambios.items():
        setattr(producto, campo, valor)

    db.commit()
    db.refresh(producto)

    return producto


def eliminar_producto(db: Session, producto_id: int):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if producto is None:
        return False
    db.delete(producto)
    db.commit()
    return True
# productos_db = [
#     {"id": 1, "nombre": "Laptop Dell", "precio": 1299.99, "stock": 15, "categoria": "tecnologia"},
#     {"id": 2, "nombre": "Mouse", "precio": 25.0, "stock": 100, "categoria": "tecnologia"},
#     {"id": 3, "nombre": "Cuaderno", "precio": 5.5, "stock": 200, "categoria": "papeleria"},
#     {"id": 4, "nombre": "Teclado Mecánico", "precio": 150.0, "stock": 40, "categoria": "tecnologia"},
#     {"id": 5, "nombre": "Monitor LG 24 pulgadas", "precio": 850.0, "stock": 12, "categoria": "tecnologia"},
#     {"id": 6, "nombre": "Impresora Epson", "precio": 620.5, "stock": 8, "categoria": "tecnologia"},
#     {"id": 7, "nombre": "Silla de Oficina", "precio": 420.0, "stock": 18, "categoria": "muebles"},
#     {"id": 8, "nombre": "Escritorio", "precio": 780.0, "stock": 10, "categoria": "muebles"},
#     {"id": 9, "nombre": "Lápiz", "precio": 1.5, "stock": 500, "categoria": "papeleria"},
#     {"id": 10, "nombre": "Borrador", "precio": 2.0, "stock": 250, "categoria": "papeleria"}
# ]
# contador_id = 11

# def obtener_producto(producto_id):
#     for p in productos_db:
#         if p["id"] == producto_id:
#             return p
#     return None


# def crear_producto(datos):
#     global contador_id
#     nuevo = {
#         "id": contador_id,
#         "nombre": datos.nombre,
#         "precio": datos.precio,
#         "stock": datos.stock,
#         "categoria": datos.categoria
#     }
#     productos_db.append(nuevo)
#     contador_id += 1
#     return nuevo


# def listar_productos(categoria=None, precio_max=None):
#     resultado = productos_db
#     if categoria is not None:
#         resultado = [p for p in resultado if p["categoria"].lower() == categoria.lower()]
#     if precio_max is not None:
#         resultado = [p for p in resultado if p["precio"] <= precio_max]
#     return resultado


# def obtener_producto(producto_id):
#     for p in productos_db:
#         if p["id"] == producto_id:
#             return p
#     return None


# def actualizar_producto(producto_id, datos):
#     for p in productos_db:
#         if p["id"] == producto_id:
#             p["nombre"] = datos.nombre
#             p["precio"] = datos.precio
#             p["stock"] = datos.stock
#             p["categoria"] = datos.categoria
#             return p
#     return None


# def eliminar_producto(producto_id):
#     for p in productos_db:
#         if p["id"] == producto_id:
#             productos_db.remove(p)
#             return True
#     return False

# def actualizar_parcial_producto(producto_id, datos):
#     for p in productos_db:
#         if p["id"] == producto_id:
#             cambios = datos.model_dump(exclude_unset=True)
#             for campo, valor in cambios.items():
#                 p[campo] = valor
#             return p
#     return None
