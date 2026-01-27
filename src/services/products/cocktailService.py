from src.infrastructure.db.repositories.products.cocktail_repository_sqlalchemy import CocktailRepositorySQLAlchemy


class CocktailService:
    def __init__(self, cocktailRepo: CocktailRepositorySQLAlchemy):
        self.repository = cocktailRepo