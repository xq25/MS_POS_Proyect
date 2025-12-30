from enum import Enum
from typing import Optional

class Ingredient:
    def __init__(self, id: Optional[int], name: str, unit: Units, status:IngredientStatus):
        self.id = id
        self.name = name
        self.unit = unit

class Units(Enum):
    GRAM = "gr"
    KILOGRAM = "kg"
    LITER = "l"
    MILLILITER = "ml"
    CUP = "Scup"
    TABLESPOON = "Cucharada"
    TEASPOON = "Cucharadita"
    PIECE = "Pisca"

class IngredientStatus(Enum):
    NORMAL = "Normal"
    STOCK_OUT = "Agotado"