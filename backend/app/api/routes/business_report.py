from pathlib import Path
import numpy as np
from fastapi import APIRouter, Request, UploadFile, Form, File, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from .. import helpers, deps
from ... import crud

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR) + "/../../../../frontend/src")

router = APIRouter(prefix="/business_report", tags=["business_reports"])


@router.get("/", response_class=HTMLResponse)
def business_report_form(request: Request, db: Session = Depends(deps.get_db)):
    business_categories = crud.get_business_categories(db)
    context = {"business_categories": business_categories}
    return templates.TemplateResponse(
        request, name="business_report.html", context=context
    )


@router.post("/", response_class=HTMLResponse)
def business_report_result(
    request: Request,
    business_name: str = Form(...),
    review_name: str = Form(...),
    radio_business_category: str = Form(...),
    csvfile: UploadFile = File(...),
):
    # Preprocessing
    df = helpers.file_handle(csvfile)
    col = helpers.extract_col(df, colname=review_name)
    col = helpers.preprocess(col=col)
    # Classify and add to the results tab
    results = {}
    models = helpers.get_models(radio_business_category)
    for name, model in models.items():
        preds = model.predict(col)
        results[name] = helpers.add_counts_with_preds(preds=preds)
    context = {"results": results, "business_name": business_name}

    return templates.TemplateResponse(
        request, name="business_report.html", context=context
    )
