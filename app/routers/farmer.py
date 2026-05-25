from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, UserLogin

router = APIRouter()

@router.get("/")
def get_farmer_data():
    return {"message": "Farmer endpoints coming soon"}

# ================= farmer signup =================
@router.post("/farmer_signup", response_model=UserResponse)
def farmer_signup(user_data: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists by phone or nid
    existing_user = db.query(User).filter(
        (User.phone == user_data.phone) | (User.nid == user_data.nid)
    ).first()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this phone or NID already exists")
    
    new_user = User(
        name=user_data.name,
        phone=user_data.phone,
        nid=user_data.nid,
        role=user_data.role, # Explicitly set role as farmer
        image_url=user_data.image_url,
        division=user_data.division,
        district=user_data.district,
        village=user_data.village
    )
    
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return UserResponse.model_validate(new_user)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

# ================= farmer login =================
@router.post("/farmer_login")
def farmer_login(user_data: UserLogin, db: Session = Depends(get_db)):
    # Check if user already exists by phone or nid
    existing_user = db.query(User).filter(
        (User.phone == user_data.phone) | (User.nid == user_data.nid)
    ).first()


    if not existing_user:
        raise HTTPException(status_code=400, detail="Invalid phone number or NID")

    # In a real app, you would generate a JWT token here
    return {
        "message": "Farmer login successful",
        "user_id": existing_user.user_id,
        "name": existing_user.name
    }