from typing import Optional

from src.domain.models.Ingredients import Ingredient

class Recipe:
    def __init__(self, id: Optional[int], name: str, ingredients: list[RecipeIngredient], instructions: str, document_link: Optional[str] = None):
        self.id = id
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.document_link = document_link

class RecipeIngredient:
    def __init__(self, ingredient: Ingredient, quantity: float):
        self.ingredient = ingredient
        self.quantity = quantity
