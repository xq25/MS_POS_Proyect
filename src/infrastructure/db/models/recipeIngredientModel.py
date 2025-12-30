# src/infrastructure/db/models/recipe_ingredient_model.py
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.infrastructure.db.base import Base

class RecipeIngredientModel(Base):
    __tablename__ = "recipe_ingredients"

    recipe_id = Column(
        Integer,
        ForeignKey("recipes.id"),
        primary_key=True
    )
    ingredient_id = Column(
        Integer,
        ForeignKey("ingredients.id"),
        primary_key=True
    )

    quantity = Column(Float, nullable=False)

    recipe = relationship(
        "RecipeModel",
        back_populates="ingredients"
    )
    ingredient = relationship(
        "IngredientModel",
        back_populates="recipes"
    )
