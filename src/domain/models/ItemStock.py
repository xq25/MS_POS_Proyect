from enum import Enum
from src.domain.models.Ingredients import Ingredient
from src.domain.models.Products import Product

class Item_Stock:
    def __init__(self, item: Product | Ingredient, item_type: Item_Type, stock: float, min_stock: float = 0.0):
        self.item = item
        self.item_type = item_type
        self.stock = stock
        self.min_stock = min_stock  # Minimum stock level, can be used for alerts or reports.

class Item_Type(Enum):
    INGREDIENT = "ingredient"
    PRODUCT = "product"