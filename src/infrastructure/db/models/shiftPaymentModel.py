# src/infrastructure/db/models/shift_payment_model.py
from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from src.infrastructure.db.base import Base

class ShiftPaymentModel(Base):
    __tablename__ = "shift_payments"

    id = Column(Integer, primary_key=True, autoincrement=True)

    payment_date = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    amount = Column(Float, nullable=False)

    # Relaciones
    shifts = relationship(
        "ShiftModel",
        back_populates="shift_payment"
    )
