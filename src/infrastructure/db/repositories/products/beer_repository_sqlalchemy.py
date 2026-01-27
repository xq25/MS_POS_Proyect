from sqlalchemy.orm import Session
from src.infrastructure.db.models.Products.beerModel import BeerModel
from src.domain.models.Products import Beer, BeerProfile
from src.infrastructure.db.repositories.product_repository_sqlalchemy import ProductRepositorySQLAlchemy

class BeerRepositorySQLAlchemy(ProductRepositorySQLAlchemy):
    '''Repositorio específico para operaciones con cervezas.
    Los commits van en los controladores después de que todas las operaciones se hayan realizado con éxito.'''
    
    def __init__(self, db: Session):
        super().__init__(db)
        self.db = db

    def get_all(self) -> list[BeerModel]:
        """Obtiene todas las cervezas."""
        return self.db.query(BeerModel).all()
    
    def get_by_id(self, beer_id: int) -> BeerModel | None:
        """Obtiene una cerveza por ID."""
        db_beer = self.db.query(BeerModel).filter(BeerModel.id == beer_id).first()
        return db_beer if db_beer else None
    
    def get_by_origin(self, origin: str) -> list[BeerModel]:
        """Obtiene cervezas por país de origen."""
        db_beers = self.db.query(BeerModel).filter(BeerModel.origin == origin).all()
        return db_beers if db_beers else []
    
    def get_by_profile(self, profile: BeerProfile) -> list[BeerModel]:
        """Obtiene cervezas por perfil (dorada, oscura, roja, verde)."""
        db_beers = self.db.query(BeerModel).filter(BeerModel.profile == profile).all()
        return db_beers if db_beers else []
    
    def get_national_beers(self) -> list[BeerModel]:
        """Obtiene todas las cervezas nacionales."""
        db_beers = self.db.query(BeerModel).filter(BeerModel.is_national == True).all()
        return db_beers if db_beers else []
    
    def get_imported_beers(self) -> list[BeerModel]:
        """Obtiene todas las cervezas importadas."""
        db_beers = self.db.query(BeerModel).filter(BeerModel.is_national == False).all()
        return db_beers if db_beers else []
    
    def get_beers_by_alcohol_range(self, min_percentage: float, max_percentage: float) -> list[BeerModel]:
        """Obtiene cervezas dentro de un rango de porcentaje de alcohol."""
        db_beers = self.db.query(BeerModel).filter(
            BeerModel.alcohol_percentage >= min_percentage,
            BeerModel.alcohol_percentage <= max_percentage
        ).all()
        return db_beers if db_beers else []
    
    def get_by_origin_and_profile(self, origin: str, profile: BeerProfile) -> list[BeerModel]:
        """Obtiene cervezas por origen y perfil combinados."""
        db_beers = self.db.query(BeerModel).filter(
            BeerModel.origin == origin,
            BeerModel.profile == profile
        ).all()
        return db_beers if db_beers else []
    
    def create(self, beer: Beer) -> BeerModel:
        """Crea una nueva cerveza en la base de datos."""
        db_beer = BeerModel(
            name=beer.name,
            price=beer.price,
            description=beer.description,
            category=beer.category,
            recipe_id=beer.recipe.id if beer.recipe else None,
            alcohol_percentage=beer.alcohol_percentage,
            profile=beer.profile,
            origin=beer.origin,
            is_national=beer.is_national
        )
        self.db.add(db_beer)
        self.db.flush()
        self.db.refresh(db_beer)
        return db_beer
    
    def update(self, beer: Beer) -> BeerModel | None:
        """Actualiza una cerveza existente."""
        db_beer = self.db.query(BeerModel).get(beer.id)
        if not db_beer:
            return None
        
        db_beer.name = beer.name
        db_beer.price = beer.price
        db_beer.description = beer.description
        db_beer.recipe_id = beer.recipe.id if beer.recipe else None
        db_beer.alcohol_percentage = beer.alcohol_percentage
        db_beer.profile = beer.profile
        db_beer.origin = beer.origin
        db_beer.is_national = beer.is_national
        
        self.db.flush()
        self.db.refresh(db_beer)
        return db_beer
    
    def delete(self, beer_id: int) -> bool:
        """Elimina una cerveza por ID."""
        db_beer = self.db.query(BeerModel).get(beer_id)
        if db_beer:
            self.db.delete(db_beer)
            self.db.flush()
            return db_beer
        return None
