from sqlalchemy.orm import Session

# Importar todos los repositorios específicos
from src.infrastructure.db.repositories.products.beer_repository_sqlalchemy import BeerRepositorySQLAlchemy
from src.infrastructure.db.repositories.products.drink_repository_sqlalchemy import DrinkRepositorySQLAlchemy
from src.infrastructure.db.repositories.products.food_repository_sqlalchemy import FoodRepositorySQLAlchemy
from src.infrastructure.db.repositories.products.cocktail_repository_sqlalchemy import CocktailRepositorySQLAlchemy
from src.infrastructure.db.repositories.products.shot_repository_sqlalchemy import ShotRepositorySQLAlchemy
from src.infrastructure.db.repositories.products.snack_repository_sqlalchemy import SnackRepositorySQLAlchemy

class ProductRepositoryFactory:
    '''Factory para crear instancias de los repositorios específicos de productos.
    Simplifica la inyección de dependencias en los servicios.'''
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_beer_repository(self) -> BeerRepositorySQLAlchemy:
        """Obtiene el repositorio de cervezas."""
        return BeerRepositorySQLAlchemy(self.db)
    
    def get_drink_repository(self) -> DrinkRepositorySQLAlchemy:
        """Obtiene el repositorio de bebidas."""
        return DrinkRepositorySQLAlchemy(self.db)
    
    def get_food_repository(self) -> FoodRepositorySQLAlchemy:
        """Obtiene el repositorio de comidas."""
        return FoodRepositorySQLAlchemy(self.db)
    
    def get_cocktail_repository(self) -> CocktailRepositorySQLAlchemy:
        """Obtiene el repositorio de cócteles."""
        return CocktailRepositorySQLAlchemy(self.db)
    
    def get_shot_repository(self) -> ShotRepositorySQLAlchemy:
        """Obtiene el repositorio de shots."""
        return ShotRepositorySQLAlchemy(self.db)
    
    def get_snack_repository(self) -> SnackRepositorySQLAlchemy:
        """Obtiene el repositorio de snacks."""
        return SnackRepositorySQLAlchemy(self.db)
