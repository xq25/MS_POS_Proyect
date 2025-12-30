from sqlalchemy import Column, Integer, Boolean, Enum, ForeignKey
from src.infrastructure.db.base import Base
from src.domain.models.Products import SnackType, FlavorProfileSnacks
from src.infrastructure.db.models.productModel import ProductModel

class SnackModel(ProductModel):
    __tablename__ = "snacks"

    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True)
    snack_type = Column(Enum(SnackType), nullable=False)
    flavor_profile = Column(Enum(FlavorProfileSnacks), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "snack"
    }