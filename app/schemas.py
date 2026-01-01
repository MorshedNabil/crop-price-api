from pydantic import BaseModel
from datetime import date

class CropPriceRequest(BaseModel):
    state: str
    district: str
    prediction_date: date
    avg_temperature: float
    avg_humidity: float
    season: str

class CropPriceResponse(BaseModel):
    predicted_price: float