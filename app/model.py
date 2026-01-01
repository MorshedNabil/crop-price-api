import joblib
import numpy as np
import os
from pathlib import Path
import pandas as pd

# Get the absolute path to the model file
MODEL_DIR = Path(__file__).parent.parent / "model"
MODEL_PATH = MODEL_DIR / "xgboost_model.joblib"

model = joblib.load(MODEL_PATH)


def preprocess(data):
    # Extract date components
    pred_date = data.prediction_date
    year = pred_date.year
    month = pred_date.month
    day = pred_date.day
    week_of_year = pred_date.isocalendar().week

    # Create a DataFrame for the single prediction with requested format
    input_data = pd.DataFrame({
        'state': [data.state],
        'district': [data.district],
        'year': [year],
        'month': [month],
        'day': [day],
        'week_of_year': [week_of_year],
        'season': [data.season],
        'avg_temperature': [data.avg_temperature],
        'avg_humidity': [data.avg_humidity]
    })
    
    return input_data


def predict_price(data):
    try:
        features = preprocess(data)
        prediction = model.predict(features)
        return float(prediction[0])
    except Exception as e:
        raise ValueError(f"Prediction failed: {str(e)}")