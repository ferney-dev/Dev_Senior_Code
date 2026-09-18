from pydantic import BaseModel

class HorarioCrear(BaseModel):
    dia_semana: str
    hora_inicio: str
    hora_fin: str

class HorarioRespuesta(BaseModel):
    id: int
    medico_id: int
    dia_semana: str
    hora_inicio: str
    hora_fin: str

    class Config:
        from_attributes = True