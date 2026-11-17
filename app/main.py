from fastapi import FastAPI
from app.routers import prediction, farmer, vendor, auth
from app.core.config import settings
from app import models

app = FastAPI(title=settings.PROJECT_NAME)

# Include Routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(prediction.router, prefix="/prediction", tags=["ML Prediction"])
app.include_router(farmer.router, prefix="/farmer", tags=["Farmer APIs"])
app.include_router(vendor.router, prefix="/vendor", tags=["Vendor APIs"])

@app.get("/")
def home():
    return {"message": f"{settings.PROJECT_NAME} is running"}
