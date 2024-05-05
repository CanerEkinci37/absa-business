from pathlib import Path
from fastapi import APIRouter, Request, UploadFile, Form, File
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from .. import helpers

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR) + "/../../../../frontend/src")

router = APIRouter(prefix="/business_report", tags=["business_reports"])


@router.get("/", response_class=HTMLResponse)
def business_report_form(request: Request):
    return templates.TemplateResponse(request, name="business_report.html")


@router.post("/", response_class=HTMLResponse)
def business_report_result(
    request: Request,
    business_name: str = Form(...),
    review_name: str = Form(...),
    csvfile: UploadFile = File(...),
):
    FOOD_MODEL, PRICE_MODEL, SERVICE_MODEL, AMBIENCE_MODEL = helpers.get_ml_models()
    business_dict = helpers.get_business_dict()

    df = helpers.file_handle(csvfile)
    col = helpers.extract_col(df, colname=review_name)
    food_results = helpers.get_model_predict_results(FOOD_MODEL, col=col)
    business_dict = helpers.add_result_to_dict(
        "FOOD", business_dict, results_dict=food_results
    )
    price_results = helpers.get_model_predict_results(PRICE_MODEL, col=col)
    business_dict = helpers.add_result_to_dict(
        "PRICE", business_dict, results_dict=price_results
    )
    service_results = helpers.get_model_predict_results(SERVICE_MODEL, col=col)
    business_dict = helpers.add_result_to_dict(
        "SERVICE", business_dict, results_dict=service_results
    )
    ambience_results = helpers.get_model_predict_results(AMBIENCE_MODEL, col=col)
    business_dict = helpers.add_result_to_dict(
        "AMBIENCE", business_dict, results_dict=ambience_results
    )
    context = {"results": business_dict, "business_name": business_name}
    return templates.TemplateResponse(
        request, name="business_report.html", context=context
    )
