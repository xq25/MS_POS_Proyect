from src.infrastructure.db.repositories.products.drink_repository_sqlalchemy import DrinkRepositorySQLAlchemy


class DrinkService:
    def __init__(self, drinkRepo: DrinkRepositorySQLAlchemy):
        self.repository = drinkRepo