from pydantic import BaseModel, Field, ConfigDict, field_validator


class ProductoCreate(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=50)
    precio: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    categoria_id: int = Field(..., gt=0)
    proveedor_id: int | None = Field(default=None, gt=0)

    @field_validator("nombre")
    @classmethod
    def limpiar_nombre(cls, valor: str) -> str:
        valor = valor.strip()
        if not valor:
            raise ValueError("El nombre no puede estar vacío")
        return valor


class ProductoUpdate(BaseModel):
    nombre: str | None = Field(default=None, min_length=3, max_length=50)
    precio: float | None = Field(default=None, gt=0)
    stock: int | None = Field(default=None, ge=0)
    categoria_id: int | None = Field(default=None, gt=0)
    proveedor_id: int | None = Field(default=None, gt=0)


class ProductoRespuesta(BaseModel):
    id: int
    nombre: str
    precio: float
    stock: int
    categoria_id: int
    proveedor_id: int | None = None

    model_config = ConfigDict(from_attributes=True)