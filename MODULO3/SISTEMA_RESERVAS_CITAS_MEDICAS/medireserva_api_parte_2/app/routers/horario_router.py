from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.horario_schema import HorarioCrear, HorarioRespuesta
from app.services.horario_service import crear_horario, eliminar_horario
from app.auth.dependencias import requerir_medico
from app.models.usuario_model import Usuario

router = APIRouter(prefix="/horarios", tags=["Horarios"])

@router.post("/", response_model=HorarioRespuesta, status_code=status.HTTP_201_CREATED)
def crear(
    datos: HorarioCrear,
    usuario: Usuario = Depends(requerir_medico),
    db: Session = Depends(get_db),
):
    try:
        return crear_horario(db, datos, usuario.id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/{horario_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar(
    horario_id: int,
    usuario: Usuario = Depends(requerir_medico),
    db: Session = Depends(get_db),
):
    try:
        eliminar_horario(db, horario_id, usuario.id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except PermissionError as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))