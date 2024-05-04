from sqlalchemy.orm import Session

from . import models, schemas


def get_business_categories(db: Session):
    return db.query(models.BusinessCategory).all()


def create_business_category(
    db: Session, business_category: schemas.BusinessCategoryCreate
):
    db_business_category = models.BusinessCategory(**business_category.model_dump())
    db.add(db_business_category)
    db.commit()
    db.refresh(db_business_category)
    return db_business_category


def get_businesses(db: Session):
    return db.query(models.Business).all()


def get_businesses_by_business_category_id(db: Session, business_category_id: int):
    return (
        db.query(models.Business)
        .filter(models.Business.business_category_id == business_category_id)
        .all()
    )


def create_business(
    db: Session, business: schemas.BusinessCreate, business_category_id: int
):
    db_business = models.Business(
        **business.model_dump(), business_category_id=business_category_id
    )
    db.add(db_business)
    db.commit()
    db.refresh(db_business)
    return db_business


def get_aspects(db: Session):
    return db.query(models.Aspect).all()


def get_aspects_by_business_category_id(db: Session, business_category_id: int):
    return (
        db.query(models.Aspect)
        .filter(models.Aspect.business_category_id == business_category_id)
        .all()
    )


def create_aspect(db: Session, aspect: schemas.AspectCreate, business_category_id):
    db_aspect = models.Aspect(
        **aspect.model_dump(), business_category_id=business_category_id
    )
    db.add(db_aspect)
    db.commit()
    db.refresh(db_aspect)
    return db_aspect


def get_business_report_by_business_id(db: Session, business_id):
    return (
        db.query(models.BusinessReport)
        .filter(models.BusinessReport.business_id == business_id)
        .first()
    )


def create_business_report(
    db: Session,
    business_id: int,
    aspect_id: int,
    negative: int,
    neutral: int,
    positive: int,
):
    db_business_report = models.BusinessReport(
        business_id=business_id,
        aspect_id=aspect_id,
        negative=negative,
        neutral=neutral,
        positive=positive,
    )
    db.add(db_business_report)
    db.commit()
    db.refresh(db_business_report)
    return db_business_report
