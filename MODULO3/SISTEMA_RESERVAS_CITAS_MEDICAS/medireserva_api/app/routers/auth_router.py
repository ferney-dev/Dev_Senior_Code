from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.usuario_schema import UsuarioCrear, UsuarioRespuesta, Token
from app.services.usuario_service import crear_usuario, autenticar_usuario
from app.auth.seguridad import crear_access_token

router = APIRouter(prefix="/auth", tags=["Autenticación"])

@router.post("/registro", response_model=UsuarioRespuesta, status_code=status.HTTP_201_CREATED)
def registrar(datos: UsuarioCrear, db: Session = Depends(get_db)):
    try:
        return crear_usuario(db, datos)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = autenticar_usuario(db, form_data.username, form_data.password)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = crear_access_token(data={"sub": str(usuario.id)})
    return Token(access_token=access_token)