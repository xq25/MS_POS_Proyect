from src.domain.models.Products import Snack
from src.domain.models.Recipes import Recipe
from src.infrastructure.db.models.Products.snackModel import SnackModel
from src.infrastructure.db.repositories.products.snack_repository_sqlalchemy import SnackRepositorySQLAlchemy

class SnackService:
    def __init__(self, snackRepo: SnackRepositorySQLAlchemy):
        self.repository = snackRepo

    def db_to_domain(self, db_model:SnackModel) -> Snack:
        return Snack(
            id = db_model.id,
            name = db_model.name,
            price = db_model.price,
            description = db_model.description,
            category = db_model.category,
            recipe = Recipe(
                id=db_model.recipe_id
            )

        )

    def get_all(self) -> list[Snack]:
        db_snacks = self.repository.get_all()