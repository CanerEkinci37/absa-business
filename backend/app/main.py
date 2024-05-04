from fastapi import FastAPI
from .api.main import api_router
from . import models
from .core import db

models.Base.metadata.create_all(bind=db.engine)

app = FastAPI()
app.include_router(api_router)
