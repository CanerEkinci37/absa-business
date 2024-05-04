from fastapi import APIRouter

from .routes import business_category, business, aspect

api_router = APIRouter()
api_router.include_router(business_category.router)
api_router.include_router(business.router)
api_router.include_router(aspect.router)
