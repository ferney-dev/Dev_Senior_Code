from sqlalchemy.orm import Session
from app.models.cita_model import Cita
from app.schemas.cita_schema import CitaCrear

def crear_cita(db: Session, datos: CitaCrear, paciente_id: int) -> Cita:
    nueva_cita = Cita(
        paciente_id=paciente_id,
        medico_id=datos.medico_id,
        horario_id=datos.horario_id,
        estado="pendiente",
    )
    db.add(nueva_cita)
    db.commit()
    db.refresh(nueva_cita)
    return nueva_cita

def listar_citas_paciente(db: Session, paciente_id: int) -> list[Cita]:
    return db.query(Cita).filter(Cita.paciente_id == paciente_id).all()

def cancelar_cita(db: Session, cita_id: int, paciente_id: int) -> Cita:
    cita = db.query(Cita).filter(Cita.id == cita_id).first()
    if not cita:
        raise ValueError("Cita no encontrada")

    if cita.paciente_id != paciente_id:
        raise PermissionError("No puedes cancelar la cita de otro paciente")

    cita.estado = "cancelada"
    db.commit()
    db.refresh(cita)
    return cita