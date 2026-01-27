from src.infrastructure.db.repositories.products.beer_repository_sqlalchemy import BeerRepositorySQLAlchemy

class BeerService:
    def __init__(self, beerRepository: BeerRepositorySQLAlchemy):
        self.repository = beerRepository

    def get_all(self):
        return self
