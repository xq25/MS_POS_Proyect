from sqlalchemy import Column, Integer, Boolean, Enum, ForeignKey
from src.infrastructure.db.base import Base
from src.domain.models.Products import CocktailProfile, MainLiquor
from src.infrastructure.db.models.productModel import ProductModel

class CocktailModel(ProductModel):
    __tablename__ = "cocktails"

    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True)
    profile = Column(Enum(CocktailProfile), nullable=False)
    main_liquor = Column(Enum(MainLiquor), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "cocktail"
    }