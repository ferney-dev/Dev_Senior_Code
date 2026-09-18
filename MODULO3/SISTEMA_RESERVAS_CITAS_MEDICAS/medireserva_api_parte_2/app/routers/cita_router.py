from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.cita_schema import CitaCrear, CitaRespuesta
from app.services.cita_service import crear_cita, listar_citas_paciente, cancelar_cita
from app.auth.dependencias import obtener_usuario_actual
from app.models.usuario_model import Usuario

router = APIRouter(prefix="/citas", tags=["Citas"])

@router.post("/", response_model=CitaRespuesta, status_code=status.HTTP_201_CREATED)
def agendar(
    datos: CitaCrear,
    usuario: Usuario = Depends(obtener_usuario_actual),
    db: Session = Depends(get_db),
):
    return crear_cita(db, datos, usuario.id)

@router.get("/mis-citas", response_model=list[CitaRespuesta])
def mis_citas(
    usuario: Usuario = Depends(obtener_usuario_actual),
    db: Session = Depends(get_db),
):
    return listar_citas_paciente(db, usuario.id)

@router.patch("/{cita_id}/cancelar", response_model=CitaRespuesta)
def cancelar(
    cita_id: int,
    usuario: Usuario = Depends(obtener_usuario_actual),
    db: Session = Depends(get_db),
):
    try:
        return cancelar_cita(db, cita_id, usuario.id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except PermissionError as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))