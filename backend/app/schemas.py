from pydantic import BaseModel


class BusinessCategoryBase(BaseModel):
    name: str


class BusinessCategoryCreate(BusinessCategoryBase):
    pass


class BusinessCategory(BusinessCategoryBase):
    id: int

    class Config:
        orm_mode = True


class BusinessBase(BaseModel):
    name: str


class BusinessCreate(BusinessBase):
    pass


class Business(BusinessBase):
    id: int
    business_category_id: int

    class Config:
        orm_mode = True


class AspectBase(BaseModel):
    name: str


class AspectCreate(AspectBase):
    pass


class Aspect(AspectBase):
    id: int
    business_category_id: int

    class Config:
        orm_mode = True
