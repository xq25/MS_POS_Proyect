# src/infrastructure/db/models/order_model.py
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.infrastructure.db.base import Base
from datetime import datetime

class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)

    total_amount = Column(Float, nullable=False)
    start_at = Column(DateTime, default=datetime.utcnow)
    last_updated = Column(DateTime, nullable=True)

    table_id = Column(Integer, ForeignKey("tables.id"), nullable=False)

    products = relationship(
        "OrderProductModel",
        back_populates="order",
        cascade="all, delete-orphan"
    )
    sale = relationship(
        "SaleModel",
        back_populates="order",
        uselist=False
    )
    table = relationship(
        "TableModel",
        back_populates="orders"
    )
