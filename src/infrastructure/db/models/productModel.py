# infrastructure/db/models/product.py
from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey
from sqlalchemy.orm import relationship
from src.infrastructure.db.base import Base
from src.domain.models.Products import Category

class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String)
    category = Column(Enum(Category), nullable=False)
    recipe_id = Column(Integer, ForeignKey("recipes.id"), nullable=True)

    type = Column(String, nullable=False)  # discriminator

    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "product"
    }

# Relación uno a uno con RecipeModel
    recipe = relationship(
        "RecipeModel",  
        back_populates="product"
    )

    orders = relationship(
        "OrderProductModel",
        back_populates="product"
    )
