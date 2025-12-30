# src/infrastructure/db/models/supplier_model.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.infrastructure.db.base import Base

class SupplierModel(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    city = Column(String(100), nullable=False)
    phone = Column(String(30), nullable=False)

    provisions = relationship(
        "ProvisionModel",
        back_populates="supplier"
    )
