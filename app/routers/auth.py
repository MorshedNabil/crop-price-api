from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login():
    return {"message": "Login endpoint coming soon"}

@router.post("/register")
def register():
    return {"message": "Register endpoint coming soon"}
