import sys
import os

# Add the project root to sys.path
sys.path.append(os.getcwd())

try:
    from app.database import SessionLocal, get_db
    from app.models import User
    from app.schemas.user import UserCreate, UserResponse
    from datetime import datetime
    import json

    # Mock user data
    data = {
        "name": "Test User",
        "phone": "01700000000",
        "nid": "1234567890",
        "division": "Dhaka",
        "district": "Dhaka",
        "village": "Test Village",
        "role": "farmer"
    }
    
    user_data = UserCreate(**data)
    print("UserCreate schema validated successfully.")

    db = SessionLocal()
    
    # Check if user already exists
    existing_user = db.query(User).filter(
        (User.phone == user_data.phone) | (User.nid == user_data.nid)
    ).first()
    
    if existing_user:
        print("User already exists, deleting for test...")
        db.delete(existing_user)
        db.commit()

    new_user = User(
        name=user_data.name,
        phone=user_data.phone,
        nid=user_data.nid,
        role=user_data.role,
        division=user_data.division,
        district=user_data.district,
        village=user_data.village
    )
    
    print("Adding user to database...")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print(f"User added with ID: {new_user.user_id}")

    print("Validating with UserResponse...")
    response = UserResponse.model_validate(new_user)
    print("Response validation successful:")
    print(response.model_dump_json(indent=2))

except Exception as e:
    print("\n--- ERROR CAUGHT ---")
    import traceback
    traceback.print_exc()
    sys.exit(1)
finally:
    if 'db' in locals():
        db.close()
