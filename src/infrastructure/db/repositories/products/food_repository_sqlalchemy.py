from sqlalchemy.orm import Session
from src.infrastructure.db.models.Products.foodModel import FoodModel
from src.domain.models.Products import Food, FoodProfile
from src.infrastructure.db.repositories.product_repository_sqlalchemy import ProductRepositorySQLAlchemy

class FoodRepositorySQLAlchemy(ProductRepositorySQLAlchemy):
    '''Repositorio específico para operaciones con comidas.
    Los commits van en los controladores después de que todas las operaciones se hayan realizado con éxito.'''
    
    def __init__(self, db: Session):
        super().__init__(db)
        self.db = db

    def get_all(self) -> list[FoodModel]:
        """Obtiene todas las comidas."""
        return self.db.query(FoodModel).all()
    
    def get_by_id(self, food_id: int) -> FoodModel | None:
        """Obtiene una comida por ID."""
        db_food = self.db.query(FoodModel).filter(FoodModel.id == food_id).first()
        return db_food if db_food else None
    
    def get_by_profile(self, profile: FoodProfile) -> list[FoodModel]:
        """Obtiene comidas por perfil de sabor (dulce, salada, agridulce, ácida, picante)."""
        db_foods = self.db.query(FoodModel).filter(FoodModel.profile == profile).all()
        return db_foods if db_foods else []
    
    def get_vegan_food(self) -> list[FoodModel]:
        """Obtiene todas las comidas veganas."""
        db_foods = self.db.query(FoodModel).filter(FoodModel.is_vegan == True).all()
        return db_foods if db_foods else []
    
    def get_non_vegan_food(self) -> list[FoodModel]:
        """Obtiene todas las comidas no veganas."""
        db_foods = self.db.query(FoodModel).filter(FoodModel.is_vegan == False).all()
        return db_foods if db_foods else []
    
    def get_for_sharing(self) -> list[FoodModel]:
        """Obtiene comidas para compartir."""
        db_foods = self.db.query(FoodModel).filter(FoodModel.for_sharing == True).all()
        return db_foods if db_foods else []
    
    def get_individual_food(self) -> list[FoodModel]:
        """Obtiene comidas individuales (no para compartir)."""
        db_foods = self.db.query(FoodModel).filter(FoodModel.for_sharing == False).all()
        return db_foods if db_foods else []
    
    def get_vegan_for_sharing(self) -> list[FoodModel]:
        """Obtiene comidas veganas para compartir."""
        db_foods = self.db.query(FoodModel).filter(
            FoodModel.is_vegan == True,
            FoodModel.for_sharing == True
        ).all()
        return db_foods if db_foods else []
    
    def get_by_profile_and_vegan(self, profile: FoodProfile, is_vegan: bool) -> list[FoodModel]:
        """Obtiene comidas por perfil y opción vegana."""
        db_foods = self.db.query(FoodModel).filter(
            FoodModel.profile == profile,
            FoodModel.is_vegan == is_vegan
        ).all()
        return db_foods if db_foods else []
    
    def create(self, food: Food) -> FoodModel:
        """Crea una nueva comida en la base de datos."""
        db_food = FoodModel(
            name=food.name,
            price=food.price,
            description=food.description,
            category=food.category,
            recipe_id=food.recipe.id if food.recipe else None,
            is_vegan=food.is_vegan,
            for_sharing=food.for_sharing,
            profile=food.profile
        )
        self.db.add(db_food)
        self.db.flush()
        self.db.refresh(db_food)
        return db_food
    
    def update(self, food: Food) -> FoodModel | None:
        """Actualiza una comida existente."""
        db_food = self.db.query(FoodModel).get(food.id)
        if not db_food:
            return None
        
        db_food.name = food.name
        db_food.price = food.price
        db_food.description = food.description
        db_food.category = food.category
        db_food.recipe_id = food.recipe.id if food.recipe else None
        db_food.is_vegan = food.is_vegan
        db_food.for_sharing = food.for_sharing
        db_food.profile = food.profile
        
        self.db.flush()
        self.db.refresh(db_food)
        return db_food
    
    def delete(self, food_id: int) -> bool:
        """Elimina una comida por ID."""
        db_food = self.db.query(FoodModel).get(food_id)
        if db_food:
            self.db.delete(db_food)
            self.db.flush()
            return True
        return False
