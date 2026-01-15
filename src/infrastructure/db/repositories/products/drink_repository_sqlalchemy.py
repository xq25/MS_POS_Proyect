from sqlalchemy.orm import Session
from src.infrastructure.db.models.Products.drinkModel import DrinkModel
from src.domain.models.Products import Drink, DrinkBases
from src.infrastructure.db.repositories.product_repository_sqlalchemy import ProductRepositorySQLAlchemy

class DrinkRepositorySQLAlchemy(ProductRepositorySQLAlchemy):
    '''Repositorio específico para operaciones con bebidas.
    Los commits van en los controladores después de que todas las operaciones se hayan realizado con éxito.'''
    
    def __init__(self, db: Session):
        super().__init__(db)
        self.db = db

    def get_all(self) -> list[DrinkModel]:
        """Obtiene todas las bebidas."""
        return self.db.query(DrinkModel).all()
    
    def get_by_id(self, drink_id: int) -> DrinkModel | None:
        """Obtiene una bebida por ID."""
        db_drink = self.db.query(DrinkModel).filter(DrinkModel.id == drink_id).first()
        return db_drink if db_drink else None
    
    def get_by_base(self, base: DrinkBases) -> list[DrinkModel]:
        """Obtiene bebidas por base (limonada, soda, tónica, leche, café, agua, vino)."""
        db_drinks = self.db.query(DrinkModel).filter(DrinkModel.base == base).all()
        return db_drinks if db_drinks else []
    
    def get_alcoholic_drinks(self) -> list[DrinkModel]:
        """Obtiene todas las bebidas alcohólicas."""
        db_drinks = self.db.query(DrinkModel).filter(DrinkModel.is_alcoholic == True).all()
        return db_drinks if db_drinks else []
    
    def get_non_alcoholic_drinks(self) -> list[DrinkModel]:
        """Obtiene todas las bebidas no alcohólicas."""
        db_drinks = self.db.query(DrinkModel).filter(DrinkModel.is_alcoholic == False).all()
        return db_drinks if db_drinks else []
    
    def get_hot_drinks(self) -> list[DrinkModel]:
        """Obtiene todas las bebidas calientes."""
        db_drinks = self.db.query(DrinkModel).filter(DrinkModel.is_hot == True).all()
        return db_drinks if db_drinks else []
    
    def get_cold_drinks(self) -> list[DrinkModel]:
        """Obtiene todas las bebidas frías."""
        db_drinks = self.db.query(DrinkModel).filter(DrinkModel.is_hot == False).all()
        return db_drinks if db_drinks else []
    
    def get_by_base_and_temperature(self, base: DrinkBases, is_hot: bool) -> list[DrinkModel]:
        """Obtiene bebidas por base y temperatura combinadas."""
        db_drinks = self.db.query(DrinkModel).filter(
            DrinkModel.base == base,
            DrinkModel.is_hot == is_hot
        ).all()
        return db_drinks if db_drinks else []
    
    def get_alcoholic_by_base(self, base: DrinkBases) -> list[DrinkModel]:
        """Obtiene bebidas alcohólicas por base."""
        db_drinks = self.db.query(DrinkModel).filter(
            DrinkModel.base == base,
            DrinkModel.is_alcoholic == True
        ).all()
        return db_drinks if db_drinks else []
    
    def create(self, drink: Drink) -> DrinkModel:
        """Crea una nueva bebida en la base de datos."""
        db_drink = DrinkModel(
            name=drink.name,
            price=drink.price,
            description=drink.description,
            category=drink.category,
            recipe_id=drink.recipe.id if drink.recipe else None,
            is_alcoholic=drink.is_alcoholic,
            base=drink.base,
            is_hot=drink.is_hot
        )
        self.db.add(db_drink)
        self.db.flush()
        self.db.refresh(db_drink)
        return db_drink
    
    def update(self, drink: Drink) -> DrinkModel | None:
        """Actualiza una bebida existente."""
        db_drink = self.db.query(DrinkModel).get(drink.id)
        if not db_drink:
            return None
        
        db_drink.name = drink.name
        db_drink.price = drink.price
        db_drink.description = drink.description
        db_drink.category = drink.category
        db_drink.recipe_id = drink.recipe.id if drink.recipe else None
        db_drink.is_alcoholic = drink.is_alcoholic
        db_drink.base = drink.base
        db_drink.is_hot = drink.is_hot
        
        self.db.flush()
        self.db.refresh(db_drink)
        return db_drink
    
    def delete(self, drink_id: int) -> bool:
        """Elimina una bebida por ID."""
        db_drink = self.db.query(DrinkModel).get(drink_id)
        if db_drink:
            self.db.delete(db_drink)
            self.db.flush()
            return True
        return False
