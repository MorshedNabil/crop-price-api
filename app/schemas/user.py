from pydantic import BaseModel, Field, field_validator
from typing import Optional, Annotated, Literal
from datetime import datetime

class UserBase(BaseModel):
    name: Annotated[str, Field(..., description="The full name of the user")]
    phone: Annotated[str, Field(..., description="The phone number of the user")]
    nid: Annotated[str, Field(..., description="The national ID of the user")]
    division: Annotated[Optional[str], Field(default=None, description="The division of the user")]
    district: Annotated[Optional[str], Field(default=None, description="The district of the user")]
    village: Annotated[Optional[str], Field(default=None, description="The village of the user")]
    two_factor_secret: Annotated[Optional[str], Field(default=None, description="The 2FA secret")]
    two_factor_recovery_codes: Annotated[Optional[str], Field(default=None, description="The 2FA recovery codes")]
    two_factor_confirmed_at: Annotated[Optional[datetime], Field(default=None, description="The 2FA confirmed at")]
    role: Annotated[Literal['farmer', 'vendor'], Field(..., description="The role of the user")]
    image_url: Annotated[Optional[str], Field(default=None, description="The image URL of the user")]

    @field_validator('phone')
    @classmethod
    def validate_phone(cls, value: str) -> str:
        if not value.isdigit():
            raise ValueError('Phone number must contain only digits')
        if len(value) != 11:
            raise ValueError('Phone number must be exactly 11 digits')
        if not value.startswith('01'):
            raise ValueError('Invalid Bangladeshi phone number format. Must start with 01')
        return value

    @field_validator('nid')
    @classmethod
    def validate_nid(cls, value: str) -> str:
        if not value.isdigit():
            raise ValueError('NID must contain only digits')
        if len(value) != 10 and len(value) != 13 and len(value) != 17:
            raise ValueError('NID must be 10, 13, or 17 digits')
        return value

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    user_id: int

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    phone: str
    nid: str
