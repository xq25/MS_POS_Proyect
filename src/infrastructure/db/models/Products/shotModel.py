from sqlalchemy import Column, Integer, Boolean, Enum, ForeignKey
from src.infrastructure.db.base import Base
from src.domain.models.Products import MainLiquor
from src.infrastructure.db.models.productModel import ProductModel

class ShotModel(ProductModel):
    __tablename__ = "shots"

    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True)
    main_liquor = Column(Enum(MainLiquor), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "shot"
    }