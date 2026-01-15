from sqlalchemy.orm import Session
from src.infrastructure.db.models.Products.shotModel import ShotModel
from src.domain.models.Products import Shot, MainLiquor
from src.infrastructure.db.repositories.product_repository_sqlalchemy import ProductRepositorySQLAlchemy

class ShotRepositorySQLAlchemy(ProductRepositorySQLAlchemy):
    '''Repositorio específico para operaciones con shots.
    Los commits van en los controladores después de que todas las operaciones se hayan realizado con éxito.'''
    
    def __init__(self, db: Session):
        super().__init__(db)
        self.db = db

    def get_all(self) -> list[ShotModel]:
        """Obtiene todos los shots."""
        return self.db.query(ShotModel).all()
    
    def get_by_id(self, shot_id: int) -> ShotModel | None:
        """Obtiene un shot por ID."""
        db_shot = self.db.query(ShotModel).filter(ShotModel.id == shot_id).first()
        return db_shot if db_shot else None
    
    def get_by_main_liquor(self, main_liquor: MainLiquor) -> list[ShotModel]:
        """Obtiene shots por licor principal (vodka, ginebra, whisky, ron, tequila, etc)."""
        db_shots = self.db.query(ShotModel).filter(ShotModel.main_liquor == main_liquor).all()
        return db_shots if db_shots else []
    
    def get_vodka_shots(self) -> list[ShotModel]:
        """Obtiene shots de vodka."""
        db_shots = self.db.query(ShotModel).filter(
            ShotModel.main_liquor == MainLiquor.VODKA
        ).all()
        return db_shots if db_shots else []
    
    def get_tequila_shots(self) -> list[ShotModel]:
        """Obtiene shots de tequila."""
        db_shots = self.db.query(ShotModel).filter(
            ShotModel.main_liquor == MainLiquor.TEQUILA
        ).all()
        return db_shots if db_shots else []
    
    def get_whisky_shots(self) -> list[ShotModel]:
        """Obtiene shots de whisky."""
        db_shots = self.db.query(ShotModel).filter(
            ShotModel.main_liquor == MainLiquor.WHISKY
        ).all()
        return db_shots if db_shots else []
    
    def get_rum_shots(self) -> list[ShotModel]:
        """Obtiene shots de ron."""
        db_shots = self.db.query(ShotModel).filter(
            ShotModel.main_liquor == MainLiquor.RUM
        ).all()
        return db_shots if db_shots else []
    
    def get_gin_shots(self) -> list[ShotModel]:
        """Obtiene shots de ginebra."""
        db_shots = self.db.query(ShotModel).filter(
            ShotModel.main_liquor == MainLiquor.GIN
        ).all()
        return db_shots if db_shots else []
    
    def get_mezcal_shots(self) -> list[ShotModel]:
        """Obtiene shots de mezcal."""
        db_shots = self.db.query(ShotModel).filter(
            ShotModel.main_liquor == MainLiquor.MEZCAL
        ).all()
        return db_shots if db_shots else []
    
    def create(self, shot: Shot) -> ShotModel:
        """Crea un nuevo shot en la base de datos."""
        db_shot = ShotModel(
            name=shot.name,
            price=shot.price,
            description=shot.description,
            category=shot.category,
            recipe_id=shot.recipe.id if shot.recipe else None,
            main_liquor=shot.main_liquor
        )
        self.db.add(db_shot)
        self.db.flush()
        self.db.refresh(db_shot)
        return db_shot
    
    def update(self, shot: Shot) -> ShotModel | None:
        """Actualiza un shot existente."""
        db_shot = self.db.query(ShotModel).get(shot.id)
        if not db_shot:
            return None
        
        db_shot.name = shot.name
        db_shot.price = shot.price
        db_shot.description = shot.description
        db_shot.category = shot.category
        db_shot.recipe_id = shot.recipe.id if shot.recipe else None
        db_shot.main_liquor = shot.main_liquor
        
        self.db.flush()
        self.db.refresh(db_shot)
        return db_shot
    
    def delete(self, shot_id: int) -> bool:
        """Elimina un shot por ID."""
        db_shot = self.db.query(ShotModel).get(shot_id)
        if db_shot:
            self.db.delete(db_shot)
            self.db.flush()
            return True
        return False
