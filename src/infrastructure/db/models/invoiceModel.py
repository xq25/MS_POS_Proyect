# src/infrastructure/db/models/invoice_model.py
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Enum,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from datetime import datetime

from src.infrastructure.db.base import Base
from src.domain.models.Invoices import Document_Type


class InvoiceModel(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, autoincrement=True)

    number = Column(String(50), nullable=False, unique=True)

    sale_id = Column(
        Integer,
        ForeignKey("sales.id"),
        nullable=False,
        unique=True
    )
    total_amount = Column(Float, nullable=False)

    taxes = Column(Float, nullable=False)

    issued_at = Column(DateTime, default=datetime.utcnow)

    # 🔹 Snapshot de datos del cliente
    client_document = Column(String(30), nullable=True)
    client_name = Column(String(150), nullable=True)
    client_email = Column(String(150), nullable=True)
    client_document_type = Column(
        Enum(Document_Type),
        nullable=True
    )

    sale = relationship(
        "SaleModel",
        back_populates="invoice"
    )
    items = relationship(
        "InvoiceItemModel",
        back_populates="invoice",
        cascade="all, delete-orphan"
    )
