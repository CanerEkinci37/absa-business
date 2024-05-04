from sqlalchemy import Column, String, ForeignKey, SmallInteger
from .core.db import Base


class BusinessCategory(Base):
    __tablename__ = "business_categories"

    id = Column(SmallInteger, primary_key=True)
    name = Column(String, unique=True, index=True)


class Business(Base):
    __tablename__ = "businesses"

    id = Column(SmallInteger, primary_key=True)
    business_category_id = Column(SmallInteger, ForeignKey("business_categories.id"))
    name = Column(String)


class Aspect(Base):
    __tablename__ = "aspects"

    id = Column(SmallInteger, primary_key=True)
    business_category_id = Column(SmallInteger, ForeignKey("business_categories.id"))
    name = Column(String)


class BusinessReport(Base):
    __tablename__ = "business_reports"

    id = Column(SmallInteger, primary_key=True)
    business_id = Column(SmallInteger, ForeignKey("businesses.id"))
    aspect_id = Column(SmallInteger, ForeignKey("aspects.id"))
    negative = Column(SmallInteger)
    neutral = Column(SmallInteger)
    positive = Column(SmallInteger)
