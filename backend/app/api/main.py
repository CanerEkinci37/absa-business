from fastapi import APIRouter

from .routes import index, business_category, business, aspect, business_report

api_router = APIRouter()
api_router.include_router(index.router)
api_router.include_router(business_category.router)
api_router.include_router(business.router)
api_router.include_router(aspect.router)
api_router.include_router(business_report.router)
