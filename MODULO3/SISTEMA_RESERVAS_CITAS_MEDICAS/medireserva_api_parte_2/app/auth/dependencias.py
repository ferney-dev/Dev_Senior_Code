from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.usuario_model import Usuario
from app.auth.seguridad import verificar_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

credenciales_invalidas = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="No se pudo validar las credenciales",
    headers={"WWW-Authenticate": "Bearer"},
)

def obtener_usuario_actual(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> Usuario:
    payload = verificar_token(token)
    if payload is None or payload.get("tipo") != "access":
        raise credenciales_invalidas

    usuario_id = payload.get("sub")
    if usuario_id is None:
        raise credenciales_invalidas

    usuario = db.query(Usuario).filter(Usuario.id == int(usuario_id)).first()
    if usuario is None:
        raise credenciales_invalidas

    return usuario

def requerir_medico(usuario: Usuario = Depends(obtener_usuario_actual)) -> Usuario:
    if usuario.rol != "medico":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Esta acción requiere rol de médico",
        )
    return usuario

def requerir_admin(usuario: Usuario = Depends(obtener_usuario_actual)) -> Usuario:
    if usuario.rol != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Esta acción requiere rol de administrador",
        )
    return usuario