# src/infrastructure/db/models/order_product_model.py
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.infrastructure.db.base import Base

class OrderProductModel(Base):
    __tablename__ = "order_products"

    id = Column(Integer, primary_key=True, autoincrement=True)

    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    order = relationship("OrderModel", back_populates="products")
    product = relationship("ProductModel", back_populates="orders")

