from sqlalchemy import (
    Column,
    Integer,
    Float,
    ForeignKey,
    String
)
from sqlalchemy.orm import relationship
from src.infrastructure.db.base import Base

class InvoiceItemModel(Base):
    __tablename__ = 'invoice_items'
 
    id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_id = Column(Integer, ForeignKey('invoices.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)

    product_name = Column(String(150), nullable=False)  

    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)
 
    # 🔹 Relationships
    invoice = relationship("InvoiceModel", back_populates="items")
    product = relationship("ProductModel", back_populates="invoices")