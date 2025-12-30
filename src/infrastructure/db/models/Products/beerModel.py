from sqlalchemy import Column, Integer, Boolean, Enum, ForeignKey, String
from src.infrastructure.db.base import Base
from src.domain.models.Products import BeerProfile
from src.infrastructure.db.models.productModel import ProductModel

class BeerModel(ProductModel):
    __tablename__ = "beers"

    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True)
    alcohol_percentage = Column(Integer, nullable=False)
    profile = Column(Enum(BeerProfile), nullable=False)
    origin = Column(String, nullable=False)
    is_national = Column(Boolean, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "beer"
    }