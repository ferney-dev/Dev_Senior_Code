from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Horario(Base):
    __tablename__ = "horarios"

    id = Column(Integer, primary_key=True, index=True)
    medico_id = Column(Integer, ForeignKey("medicos.id"), nullable=False)
    dia_semana = Column(String, nullable=False)   # ej: "lunes"
    hora_inicio = Column(String, nullable=False)  # ej: "08:00"
    hora_fin = Column(String, nullable=False)     # ej: "12:00"

    medico = relationship("Medico")