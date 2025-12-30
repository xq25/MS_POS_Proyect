from sqlalchemy import Column, Integer, Float, String, UniqueConstraint, Enum
from sqlalchemy.orm import relationship
from src.infrastructure.db.base import Base
from src.domain.models.ItemStock import Item_Type

class ItemStockModel(Base):
    __tablename__ = "item_stocks"

    id = Column(Integer, primary_key=True, autoincrement=True)

    # Polimorfismo manual
    item_type = Column(Enum(Item_Type), nullable=False)  
    # valores esperados: "product" | "ingredient"

    item_id = Column(Integer, nullable=False)

    stock = Column(Float, nullable=False)
    min_stock = Column(Float, nullable=False, default=0.0)

    __table_args__ = (
        UniqueConstraint("item_type", "item_id", name="uq_item_stock"),
    )

    provisions = relationship(
        "ProvisionItemModel",
        back_populates="item_stock"
    )