from fastapi import FastAPI
from app.schemas import CropPriceRequest, CropPriceResponse
from app.model import predict_price

app = FastAPI(title="Crop Price Prediction API")

@app.post("/predict", response_model=CropPriceResponse)
def predict(data: CropPriceRequest):
    price = predict_price(data)
    return {"predicted_price": round(price, 2)}
@app.get("/")
def home():
    return {"message": "FastAPI is running on port 9000"}
