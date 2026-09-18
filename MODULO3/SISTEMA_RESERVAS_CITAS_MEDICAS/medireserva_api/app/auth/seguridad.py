from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt
from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashear_password(password: str) -> str:
    return pwd_context.hash(password)

def verificar_password(password_plano: str, password_hash: str) -> bool:
    return pwd_context.verify(password_plano, password_hash)

def crear_access_token(data: dict) -> str:
    to_encode = data.copy()
    expira = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp": expira})
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)