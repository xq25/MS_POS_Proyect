# src/infrastructure/db/models/shift_model.py
from sqlalchemy import Column, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.infrastructure.db.base import Base


class ShiftModel(Base):
    __tablename__ = "shifts"

    id = Column(Integer, primary_key=True, autoincrement=True)

    employee_id = Column(
        Integer,
        ForeignKey("employees.id"),
        nullable=False
    )

    start_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    end_at = Column(DateTime, nullable=True)

    is_active = Column(Boolean, default=True, nullable=False)

    # FOREIGN KEY that references the shift payment
    shift_payment_id = Column(
        Integer,
        ForeignKey("shift_payments.id"),
        nullable=True   # because it may not be paid yet
    )

    # Relaciones
    employee = relationship("EmployeeModel", back_populates="shifts")
    shift_payment = relationship("ShiftPaymentModel", back_populates="shifts")
