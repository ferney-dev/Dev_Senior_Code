from sqlalchemy.orm import Session
from app.models.horario_model import Horario
from app.models.medico_model import Medico
from app.schemas.horario_schema import HorarioCrear

def crear_horario(db: Session, datos: HorarioCrear, usuario_id: int) -> Horario:
    medico = db.query(Medico).filter(Medico.usuario_id == usuario_id).first()
    if not medico:
        raise ValueError("El usuario no tiene un perfil de médico")

    nuevo_horario = Horario(medico_id=medico.id, **datos.model_dump())
    db.add(nuevo_horario)
    db.commit()
    db.refresh(nuevo_horario)
    return nuevo_horario

def obtener_horario(db: Session, horario_id: int) -> Horario | None:
    return db.query(Horario).filter(Horario.id == horario_id).first()

def eliminar_horario(db: Session, horario_id: int, usuario_id: int) -> None:
    horario = obtener_horario(db, horario_id)
    if not horario:
        raise ValueError("Horario no encontrado")

    medico = db.query(Medico).filter(Medico.usuario_id == usuario_id).first()
    if not medico or horario.medico_id != medico.id:
        raise PermissionError("No puedes modificar el horario de otro médico")

    db.delete(horario)
    db.commit()