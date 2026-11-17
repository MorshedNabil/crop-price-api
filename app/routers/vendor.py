from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_vendor_data():
    return {"message": "Vendor endpoints coming soon"}
