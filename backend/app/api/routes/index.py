from pathlib import Path
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


BASE_DIR = Path(__file__).resolve().parent

router = APIRouter(tags=["index"])
templates = Jinja2Templates(directory=str(BASE_DIR) + "/../../../../frontend/src")


@router.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(request, name="index.html")
