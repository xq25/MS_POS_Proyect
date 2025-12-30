from sqlalchemy import Column, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from src.infrastructure.db.base import Base
class ProvisionItemModel(Base):
    __tablename__ = "provision_items"

    provision_id = Column(
        Integer,
        ForeignKey("provisions.id"),
        primary_key=True
    )

    item_stock_id = Column(
        Integer,
        ForeignKey("item_stocks.id"),
        primary_key=True
    )

    quantity = Column(Float, nullable=False)
    #unit_cost = Column(Float, nullable=False)  # 🔥 clave para contabilidad

    provision = relationship(
        "ProvisionModel",
        back_populates="items"
    )

    item_stock = relationship(
        "ItemStockModel",
        back_populates="provisions"
    )
