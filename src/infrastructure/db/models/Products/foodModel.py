from sqlalchemy import Column, Integer, Boolean, Enum, ForeignKey
from src.infrastructure.db.base import Base
from src.domain.models.Products import FoodProfile
from src.infrastructure.db.models.productModel import ProductModel

class FoodModel(ProductModel):
    __tablename__ = "foods"

    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True)
    is_vegan = Column(Boolean, nullable=False)
    for_sharing = Column(Boolean, nullable=False)
    profile = Column(Enum(FoodProfile), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "food"
    }
