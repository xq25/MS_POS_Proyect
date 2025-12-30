from sqlalchemy import Column, Integer, Float, String, Enum
from sqlalchemy.orm import relationship
from src.infrastructure.db.base import Base
from src.domain.models.Ingredients import Units, IngredientStatus
class IngredientModel(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(100), nullable=False, unique=True)

    unit = Column(Enum(Units), nullable=False)

    status = Column(Enum(IngredientStatus), default=IngredientStatus.AVAILABLE, nullable=False)

    recipes = relationship(
        "RecipeIngredientModel",
        back_populates="ingredient"
    )
