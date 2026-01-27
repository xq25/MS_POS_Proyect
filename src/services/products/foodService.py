from src.infrastructure.db.repositories.products.food_repository_sqlalchemy import FoodRepositorySQLAlchemy


class FoodService:
    def __init__(self, foodRepo: FoodRepositorySQLAlchemy):
        self.repository = foodRepo