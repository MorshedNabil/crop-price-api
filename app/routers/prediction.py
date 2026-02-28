from fastapi import APIRouter, HTTPException
from app.schemas.crop import CropPriceRequest, CropPriceResponse
from app.services.prediction_service import predict_price

router = APIRouter()

@router.post("/predict", response_model=CropPriceResponse)
def predict(data: CropPriceRequest):
    try:
        price = predict_price(data)
        return {"predicted_price": round(price, 2)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
