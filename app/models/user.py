from sqlalchemy import Column, String, Text, Enum, TIMESTAMP
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(BIGINT(unsigned=True), primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    phone = Column(String(11), nullable=False, unique=True)
    nid = Column(String(20), nullable=False, unique=True)
    division = Column(String(50), nullable=True)
    district = Column(String(50), nullable=True)
    village = Column(String(50), nullable=True)
    two_factor_secret = Column(Text, nullable=True)
    two_factor_recovery_codes = Column(Text, nullable=True)
    two_factor_confirmed_at = Column(TIMESTAMP, nullable=True)
    role = Column(Enum('farmer', 'vendor'), nullable=False)
    image_url = Column(String(50), nullable=True)

    # Relationships
    created_products = relationship("FarmerProduct", foreign_keys="FarmerProduct.farmer_product_creator", back_populates="creator")

    edited_products = relationship("FarmerProduct", foreign_keys="FarmerProduct.farmer_product_editor", back_populates="editor")
