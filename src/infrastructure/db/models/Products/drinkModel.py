# infrastructure/db/models/drink.py
from sqlalchemy import Column, Integer, Boolean, Enum, ForeignKey
from src.infrastructure.db.base import Base
from src.domain.models.Products import DrinkBases
from src.infrastructure.db.models.productModel import ProductModel

class DrinkModel(ProductModel):
    __tablename__ = "drinks"

    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True)
    is_alcoholic = Column(Boolean, nullable=False)
    base = Column(Enum(DrinkBases), nullable=False)
    is_hot = Column(Boolean, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "drink"
    }
