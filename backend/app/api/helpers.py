import re
import os
from io import BytesIO
from pathlib import Path
from fastapi import UploadFile
import numpy as np
import pandas as pd
import spacy
import nltk
from nltk.corpus import stopwords
from zemberek import TurkishMorphology, TurkishSentenceNormalizer
import joblib


nlp = spacy.load("tr_core_news_md")


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


def get_models(category):
    model_dict = {}
    current_path = path / f"../saved_models/{category}"
    file_list = os.listdir(current_path)
    for file in file_list:
        with open(current_path / file, "rb") as f:
            model = joblib.load(f)
        name = file.split("_")[0]
        model_dict[name] = model
    print(model_dict)
    return model_dict


def add_counts_with_preds(preds):
    unique, counts = np.unique(preds, return_counts=True)
    sentiment_dict = dict(zip(unique, counts))
    results = {
        "NEGATIVE": sentiment_dict.get(-1, 0),
        "NEUTRAL": sentiment_dict.get(0, 0),
        "POSITIVE": sentiment_dict.get(1, 0),
    }
    return results


def preprocess(col):
    nltk.download("punkt")
    stop_words = set(stopwords.words("turkish"))
    morphology = TurkishMorphology.create_with_defaults()
    sentence_normalizer = TurkishSentenceNormalizer(morphology)
    for i in range(len(col)):
        text = col[i]
        text = sentence_normalizer.normalize(text).lower()
        text = re.sub("[^a-zA-Zçğıöşü ]+", "", text)
        text = re.sub("[ ]+", " ", text)
        doc = nlp(text)
        filtered_tokens = [
            token.lemma_
            for token in doc
            if token.text not in stop_words and not token.is_oov
        ]
        col[i] = " ".join(filtered_tokens)

    return col


def get_model_predict_results(model, col):
    preds = model.predict(col)
    unique, counts = np.unique(preds, return_counts=True)
    # {-1: preds, 0:preds, 1:preds}
    result_dict = dict(zip(unique, counts))
    return result_dict
