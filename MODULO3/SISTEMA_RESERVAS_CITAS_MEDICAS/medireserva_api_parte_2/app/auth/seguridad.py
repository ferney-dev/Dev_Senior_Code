from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt, JWTError
from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashear_password(password: str) -> str:
    return pwd_context.hash(password)

def verificar_password(password_plano: str, password_hash: str) -> bool:
    return pwd_context.verify(password_plano, password_hash)

def crear_access_token(data: dict) -> str:
    to_encode = data.copy()
    expira = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp": expira, "tipo": "access"})
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)

def crear_refresh_token(data: dict) -> str:
    to_encode = data.copy()
    expira = datetime.utcnow() + timedelta(days=7)
    to_encode.update({"exp": expira, "tipo": "refresh"})
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)

def verificar_token(token: str) -> dict | None:
    try:
        return jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
    except JWTError:
        return None