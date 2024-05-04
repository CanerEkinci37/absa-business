from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import deps
from ... import schemas, crud

router = APIRouter(prefix="/business_categories", tags=["business_categories"])


@router.post("/", response_model=schemas.BusinessCategory)
def create_business_category(
    business_category: schemas.BusinessCategoryCreate,
    db: Session = Depends(deps.get_db),
):
    return crud.create_business_category(db, business_category=business_category)


@router.get("/", response_model=schemas.BusinessCategory)
def read_business_categories(db: Session = Depends(deps.get_db)):
    business_categories = crud.get_business_categories(db)
    return business_categories
