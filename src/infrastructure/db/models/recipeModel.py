# src/infrastructure/db/models/recipe_model.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from src.infrastructure.db.base import Base

class RecipeModel(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    instructions = Column(Text, nullable=False)
    document_link = Column(String(255), nullable=True)

    ingredients = relationship(
        "RecipeIngredientModel",
        back_populates="recipe",
        cascade="all, delete-orphan"
    )
    product = relationship(
        "ProductModel",
        back_populates="recipe",
        uselist=False
    )
