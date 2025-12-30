from sqlalchemy import Column, Integer, Float, DateTime, String, Enum
from src.infrastructure.db.base import Base
from src.domain.models.Expenses import ExpenseTypes
from datetime import datetime


class ExpenseModel(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, autoincrement=True)

    amount = Column(Float, nullable=False)

    type = Column(
        Enum(ExpenseTypes),
        nullable=False
    )

    expense_date = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    description = Column(String(255), nullable=True)
