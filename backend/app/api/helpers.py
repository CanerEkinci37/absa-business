from io import BytesIO
from pathlib import Path
from fastapi import UploadFile
import numpy as np
import pandas as pd
import joblib


def file_handle(file: UploadFile):
    try:
        contents = file.file.read()
    finally:
        file.close()
    contents_byte = BytesIO(contents)
    df = pd.read_csv(contents_byte)
    return df


def extract_col(df, colname):
    col = getattr(df, colname)
    col = np.array(col)
    return col


path = Path(__file__).parent


def get_ml_models():
    with open(path / "../saved_models/restaurant/food_model.joblib", "rb") as f:
        food_model = joblib.load(f)
    with open(path / "../saved_models/restaurant/price_model.joblib", "rb") as f:
        price_model = joblib.load(f)
    with open(path / "../saved_models/restaurant/service_model.joblib", "rb") as f:
        service_model = joblib.load(f)
    with open(path / "../saved_models/restaurant/ambience_model.joblib", "rb") as f:
        ambience_model = joblib.load(f)
    return food_model, price_model, service_model, ambience_model


def get_model_predict_results(model, col):
    preds = model.predict(col)
    unique, counts = np.unique(preds, return_counts=True)
    # {-1: preds, 0:preds, 1:preds}
    result_dict = dict(zip(unique, counts))
    return result_dict


def get_business_dict():
    business_dict = {"FOOD": {}, "PRICE": {}, "SERVICE": {}, "AMBIENCE": {}}
    return business_dict


def add_result_to_dict(aspect, business_dict, results_dict):
    business_dict[aspect]["NEGATIVE"] = results_dict[-1]
    business_dict[aspect]["NEUTRAL"] = results_dict[0]
    business_dict[aspect]["POSITIVE"] = results_dict[1]
    return business_dict
