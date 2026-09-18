from sqlalchemy.orm import Session

from app.models.categoria_model import Categoria
from app.schemas.categoria_schemas import CategoriaCreate


def crear_categoria(db: Session, datos: CategoriaCreate):
    nueva = Categoria(
        nombre=datos.nombre,
        descripcion=datos.descripcion,
    )

    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    return nueva


def listar_categorias(db: Session):
    return db.query(Categoria).all()


def obtener_categoria(db: Session, categoria_id: int):
    return (
        db.query(Categoria)
        .filter(Categoria.id == categoria_id)
        .first()
    )


def actualizar_categoria(db: Session, categoria_id: int, datos: CategoriaCreate):
    categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if categoria is None:
        return None
    categoria.nombre = datos.nombre
    categoria.descripcion = datos.descripcion
    db.commit()
    db.refresh(categoria)
    return categoria


def eliminar_categoria(db: Session, categoria_id: int):
    categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if categoria is None:
        return False
    db.delete(categoria)
    db.commit()
    return True



# from app.exceptions import CategoriaNoEncontrada

# categorias = []


# def obtener_categoria(categoria_id: int):
#     for categoria in categorias:
#         if categoria["id"] == categoria_id:
#             return categoria
#     raise CategoriaNoEncontrada(categoria_id)


# categorias_db = []
# contador_id = 1

# def crear_categoria(datos):
#     global contador_id
#     nueva = {
#         "id": contador_id,
#         "nombre": datos.nombre
#     }
#     categorias_db.append(nueva)
#     contador_id += 1
#     return nueva

# def listar_categorias():
#     return categorias_db


# def obtener_categoria(categoria_id):
#     for c in categorias_db:
#         if c["id"] == categoria_id:
#             return c
#     return None

# def actualizar_categoria(categoria_id, datos):
#     for c in categorias_db:
#         if c["id"] == categoria_id:
#             c["nombre"] = datos.nombre
#             return c
#     return None


# def eliminar_categoria(categoria_id):
#     for c in categorias_db:
#         if c["id"] == categoria_id:
#             categorias_db.remove(c)
#             return True
#     return False