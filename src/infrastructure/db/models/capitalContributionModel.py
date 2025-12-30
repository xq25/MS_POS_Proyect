from sqlalchemy import Column, Integer, Float, DateTime, String
from datetime import datetime
from src.infrastructure.db.base import Base


class CapitalContributionModel(Base):
    __tablename__ = "capital_contributions"

    id = Column(Integer, primary_key=True, autoincrement=True)

    amount = Column(Float, nullable=False)

    date = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )
    description = Column(String(255), nullable=True)
