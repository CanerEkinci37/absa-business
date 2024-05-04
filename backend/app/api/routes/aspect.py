from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from .. import deps
from ... import schemas, crud

router = APIRouter(prefix="/aspects", tags=["aspects"])


@router.post("/", response_model=schemas.Aspect)
def create_aspect(
    business_category_id: int,
    aspect: schemas.AspectCreate,
    db: Session = Depends(deps.get_db),
):
    return crud.create_aspect(
        db, aspect=aspect, business_category_id=business_category_id
    )


@router.get("/", response_model=list[schemas.Aspect])
def read_aspects(db: Session = Depends(deps.get_db)):
    aspects = crud.get_aspects(db)
    return aspects


@router.get("/{business_category_id}/", response_model=list[schemas.Aspect])
def read_aspects_by_category(
    business_category_id: int, db: Session = Depends(deps.get_db)
):
    aspects = crud.get_aspects_by_business_category_id(
        db, business_category_id=business_category_id
    )
    return aspects
