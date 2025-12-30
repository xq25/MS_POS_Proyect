# src/infrastructure/db/models/provision_model.py
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.infrastructure.db.base import Base

class ProvisionModel(Base):
    __tablename__ = "provisions"

    id = Column(Integer, primary_key=True, autoincrement=True)

    supplier_id = Column(
        Integer,
        ForeignKey("suppliers.id"),
        nullable=True
    )

    total_cost = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)

    supplier = relationship(
        "SupplierModel",
        back_populates="provisions"
    )

    items = relationship(
        "ProvisionItemModel",
        back_populates="provision"
    )
