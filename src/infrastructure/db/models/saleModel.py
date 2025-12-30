from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum, Float
from sqlalchemy.orm import relationship
from datetime import datetime

from src.infrastructure.db.base import Base
from src.domain.models.Sales import Payment_Method

class SaleModel(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)

    order_id = Column(
        Integer,
        ForeignKey("orders.id", ondelete="RESTRICT"),
        nullable=False,
        unique=True  # una orden solo puede generar una venta
    )

    total_amount = Column(Float, nullable=False)
    payment_method = Column(
        Enum(Payment_Method),
        nullable=False
    )

    recorded_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )
    taxes = Column(Float, nullable=False)

    # relaciones
    order = relationship("OrderModel", back_populates="sale")
    invoice = relationship("InvoiceModel", back_populates="sale", uselist=False)  # una venta tiene una factura
