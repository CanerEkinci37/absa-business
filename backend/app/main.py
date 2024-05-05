from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from .api.main import api_router
from . import models
from .core import db

BASE_DIR = Path(__file__).resolve().parent
models.Base.metadata.create_all(bind=db.engine)

app = FastAPI()
app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR) + "/../../frontend/src/static"),
    name="static",
)

app.include_router(api_router)
