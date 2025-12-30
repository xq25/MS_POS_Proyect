from sqlalchemy import Column, Integer, Float, DateTime, String
from datetime import datetime
from src.infrastructure.db.base import Base

class IncomeModel(Base):
    __tablename__ = "incomes"

    id = Column(Integer, primary_key=True, autoincrement=True)

    total_day_amount = Column(Float, nullable=False)

    date = Column(DateTime, nullable=False, default=datetime.utcnow)

    source = Column(String(100), nullable=False, default="Ventas")
