from pydantic import BaseModel, EmailStr

class UsuarioCrear(BaseModel):
    nombre: str
    email: EmailStr
    password: str

class UsuarioRespuesta(BaseModel):
    id: int
    nombre: str
    email: EmailStr
    rol: str

    class Config:
        from_attributes = True
        
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"