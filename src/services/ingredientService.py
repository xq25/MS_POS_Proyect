from src.domain.models.Ingredients import Ingredient, Units, IngredientStatus
from src.infrastructure.db.models.ingredientModel import IngredientModel
from src.infrastructure.db.repositories.ingredient_repository_sqlalchemy import IngredientRepositorySQLAlchemy


class IngredientService:
    def __init__(self, ingredientRepo: IngredientRepositorySQLAlchemy):
        self.repository = ingredientRepo

    def db_to_domain(self, db_model: IngredientModel) -> Ingredient:
        return  Ingredient(
            id= db_model.id,
            name=db_model.name,
            unit=db_model.unit,
            status=db_model.status
        )
    
    def get_all(self) -> list[Ingredient] | list:
        db_ingredients = self.repository.get_all()

        if not db_ingredients:
            return []
        return [self.db_to_domain(i) for i in db_ingredients]
        
    def get_by_id(self, id:int) -> Ingredient:
        db_ingredient = self.repository.get_by_id(id)

        if not db_ingredient:
            raise ValueError(f'El ingrediente con id {id} no ha sido encontrado')
        
        return self.db_to_domain(db_ingredient)

    def get_by_unit(self, unit: Units) -> list[Ingredient] | list:
        db_ingredients = self.repository.get_by_unit(unit)

        if not db_ingredients:
            return []
        return [self.db_to_domain(i) for i in db_ingredients]
    
    def get_by_status(self, status: IngredientStatus) -> list[Ingredient] | list:
        db_ingredients = self.repository.get_by_status(status)

        if not db_ingredients:
            return []
        return [self.db_to_domain(i) for i in db_ingredients]
    
    def create(self, ingredient:Ingredient) -> Ingredient:
        db_ingredient = self.repository.create(ingredient)

        return self.db_to_domain(db_ingredient)
    
    def update(self, ingredient:Ingredient) -> Ingredient:
        db_ingredient_updated = self.repository.update(ingredient)

        if not db_ingredient_updated:
            raise ValueError(f'El ingrediente con id {ingredient.id} no ha sido encontrado')
        
        return self.db_to_domain(db_ingredient_updated)
    
    def delete(self, id:int) -> Ingredient:
        db_ingredient_deleted = self.repository.delete(id)

        if not db_ingredient_deleted:
            raise ValueError(f'El ingrediente con id {id} no ha sido encontrado')

        return db_ingredient_deleted
    