from sqlalchemy.orm import Session
from app.models.usuario_model import Usuario
from app.schemas.usuario_schema import UsuarioCrear
from app.auth.seguridad import hashear_password, verificar_password

def obtener_usuario_por_email(db: Session, email: str) -> Usuario | None:
    return db.query(Usuario).filter(Usuario.email == email).first()

def crear_usuario(db: Session, datos: UsuarioCrear) -> Usuario:
    usuario_existente = obtener_usuario_por_email(db, datos.email)
    if usuario_existente:
        raise ValueError("El email ya está registrado")

    nuevo_usuario = Usuario(
        nombre=datos.nombre,
        email=datos.email,
        password_hash=hashear_password(datos.password),
        rol="paciente",  # fijado en el servidor, no lo decide quien se registra
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

def autenticar_usuario(db: Session, email: str, password: str) -> Usuario | None:
    usuario = obtener_usuario_por_email(db, email)
    if not usuario:
        return None
    if not verificar_password(password, usuario.password_hash):
        return None
    return usuario