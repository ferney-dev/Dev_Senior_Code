from pydantic import BaseModel

class CitaCrear(BaseModel):
    medico_id: int
    horario_id: int

class CitaRespuesta(BaseModel):
    id: int
    paciente_id: int
    medico_id: int
    horario_id: int
    estado: str

    class Config:
        from_attributes = True