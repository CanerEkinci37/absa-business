from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import deps
from ... import schemas, crud

router = APIRouter(prefix="/businesses", tags=["businesses"])


@router.post("/", response_model=schemas.Business)
def create_business(
    business_category_id: int,
    business: schemas.BusinessCreate,
    db: Session = Depends(deps.get_db),
):
    return crud.create_business(
        db, business=business, business_category_id=business_category_id
    )


@router.get("/", response_model=list[schemas.Business])
def read_businesses(db: Session = Depends(deps.get_db)):
    businesses = crud.get_businesses(db)
    return businesses


@router.get("/{business_category_id}/")
def read_businesses_by_category(
    business_category_id: int, db: Session = Depends(deps.get_db)
):
    businesses = crud.get_businesses_by_business_category_id(
        db, business_category_id=business_category_id
    )
    return businesses
