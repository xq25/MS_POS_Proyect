from sqlalchemy.orm import Session
from src.domain.models.Ingredients import Ingredient, Units, IngredientStatus
from src.infrastructure.db.models.ingredientModel import IngredientModel

class IngredientRepositorySQLAlchemy:
    
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[IngredientModel]:
        db_ingredients = self.db.query(IngredientModel).all()

    def get_by_id(self, id:int) -> IngredientModel:
        db_ingredient = self.db.query(IngredientModel).filter(IngredientModel.id == id).first()

        return db_ingredient
    
    def get_by_unit(self, unit: Units) -> list[IngredientModel]:
        db_ingredients = self.db.query(IngredientModel).filter(IngredientModel.unit == unit).all()

    def get_by_status(self, status: IngredientStatus) -> list[IngredientModel]:
        db_ingredients = self.db.query(IngredientModel).filter(IngredientModel.status == status).all()
    
    def create(self, ingredient:Ingredient) -> IngredientModel:
        db_ingredient = IngredientModel(
            name=ingredient.name,
            unit=ingredient.unit,
            status=ingredient.status
        )
        self.db.add(db_ingredient)
        self.db.flush()
        self.db.refresh(db_ingredient)

        return db_ingredient
    
    def update(self, ingredient: Ingredient) -> IngredientModel:
        db_ingredient = self.db.query(IngredientModel).get(ingredient.id)

        if not db_ingredient:
            return None
        
        db_ingredient.name = ingredient.name
        db_ingredient.unit = ingredient.unit
        db_ingredient.status = ingredient.status

        self.db.flush()
        self.db.refresh(db_ingredient)

        return db_ingredient
    
    def delete(self, ingredient_id:int) -> IngredientModel:
        db_ingredient = self.db.query(IngredientModel).get(ingredient_id)

        if not db_ingredient:
            return None
        
        self.db.delete(db_ingredient)
        self.db.flush()

        return db_ingredient
