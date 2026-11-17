from sqlalchemy import Column, String, Integer, DECIMAL, Date, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.mysql import BIGINT, TINYINT
from sqlalchemy.orm import relationship
from app.database import Base

class FarmerProduct(Base):
    __tablename__ = "farmer_products"

    farmer_product_id = Column(BIGINT(unsigned=True), primary_key=True, autoincrement=True)
    farmer_product_image = Column(String(50), nullable=True)
    farmer_product_name = Column(String(50), nullable=True)
    farmer_product_Details = Column(String(200), nullable=True)
    farmer_product_price = Column(DECIMAL(10, 2), nullable=True)
    quantity = Column(Integer, nullable=False, default=1)
    farmer_phone_number = Column(String(20), nullable=True)
    farmer_post_date = Column(Date, nullable=True)
    
    # Foreign Keys
    farmer_product_creator = Column(BIGINT(unsigned=True), ForeignKey("users.user_id"), nullable=False)
    farmer_product_editor = Column(BIGINT(unsigned=True), ForeignKey("users.user_id"), nullable=False)
    
    farmer_product_status = Column(TINYINT(1), nullable=False, default=0)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True)

    # Relationships
    creator = relationship("User", foreign_keys=[farmer_product_creator], back_populates="created_products")
    editor = relationship("User", foreign_keys=[farmer_product_editor], back_populates="edited_products")
