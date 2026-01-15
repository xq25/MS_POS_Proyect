from sqlalchemy.orm import Session
from src.infrastructure.db.models.Products.snackModel import SnackModel
from src.domain.models.Products import Snack, SnackType, FlavorProfileSnacks
from src.infrastructure.db.repositories.product_repository_sqlalchemy import ProductRepositorySQLAlchemy

class SnackRepositorySQLAlchemy(ProductRepositorySQLAlchemy):
    '''Repositorio específico para operaciones con snacks.
    Los commits van en los controladores después de que todas las operaciones se hayan realizado con éxito.'''
    
    def __init__(self, db: Session):
        super().__init__(db)
        self.db = db

    def get_all(self) -> list[SnackModel]:
        """Obtiene todos los snacks."""
        return self.db.query(SnackModel).all()
    
    def get_by_id(self, snack_id: int) -> SnackModel | None:
        """Obtiene un snack por ID."""
        db_snack = self.db.query(SnackModel).filter(SnackModel.id == snack_id).first()
        return db_snack if db_snack else None
    
    def get_by_snack_type(self, snack_type: SnackType) -> list[SnackModel]:
        """Obtiene snacks por tipo (postre, pastelería, panadería, dulce)."""
        db_snacks = self.db.query(SnackModel).filter(SnackModel.snack_type == snack_type).all()
        return db_snacks if db_snacks else []
    
    def get_by_flavor_profile(self, flavor_profile: FlavorProfileSnacks) -> list[SnackModel]:
        """Obtiene snacks por perfil de sabor (dulce, salado, agridulce, picante)."""
        db_snacks = self.db.query(SnackModel).filter(SnackModel.flavor_profile == flavor_profile).all()
        return db_snacks if db_snacks else []
    
    def get_desserts(self) -> list[SnackModel]:
        """Obtiene postres."""
        db_snacks = self.db.query(SnackModel).filter(
            SnackModel.snack_type == SnackType.DESSERT
        ).all()
        return db_snacks if db_snacks else []
    
    def get_pastries(self) -> list[SnackModel]:
        """Obtiene pastelería."""
        db_snacks = self.db.query(SnackModel).filter(
            SnackModel.snack_type == SnackType.PASTRY
        ).all()
        return db_snacks if db_snacks else []
    
    def get_bakery(self) -> list[SnackModel]:
        """Obtiene productos de panadería."""
        db_snacks = self.db.query(SnackModel).filter(
            SnackModel.snack_type == SnackType.BAKERY
        ).all()
        return db_snacks if db_snacks else []
    
    def get_sweet_snacks(self) -> list[SnackModel]:
        """Obtiene snacks dulces."""
        db_snacks = self.db.query(SnackModel).filter(
            SnackModel.flavor_profile == FlavorProfileSnacks.SWEET
        ).all()
        return db_snacks if db_snacks else []
    
    def get_salty_snacks(self) -> list[SnackModel]:
        """Obtiene snacks salados."""
        db_snacks = self.db.query(SnackModel).filter(
            SnackModel.flavor_profile == FlavorProfileSnacks.SALTY
        ).all()
        return db_snacks if db_snacks else []
    
    def get_spicy_snacks(self) -> list[SnackModel]:
        """Obtiene snacks picantes."""
        db_snacks = self.db.query(SnackModel).filter(
            SnackModel.flavor_profile == FlavorProfileSnacks.SPICY
        ).all()
        return db_snacks if db_snacks else []
    
    def get_by_type_and_flavor(self, snack_type: SnackType, flavor_profile: FlavorProfileSnacks) -> list[SnackModel]:
        """Obtiene snacks por tipo y perfil de sabor combinados."""
        db_snacks = self.db.query(SnackModel).filter(
            SnackModel.snack_type == snack_type,
            SnackModel.flavor_profile == flavor_profile
        ).all()
        return db_snacks if db_snacks else []
    
    def create(self, snack: Snack) -> SnackModel:
        """Crea un nuevo snack en la base de datos."""
        db_snack = SnackModel(
            name=snack.name,
            price=snack.price,
            description=snack.description,
            category=snack.category,
            recipe_id=snack.recipe.id if snack.recipe else None,
            snack_type=snack.snack_type,
            flavor_profile=snack.flavor_profile
        )
        self.db.add(db_snack)
        self.db.flush()
        self.db.refresh(db_snack)
        return db_snack
    
    def update(self, snack: Snack) -> SnackModel | None:
        """Actualiza un snack existente."""
        db_snack = self.db.query(SnackModel).get(snack.id)
        if not db_snack:
            return None
        
        db_snack.name = snack.name
        db_snack.price = snack.price
        db_snack.description = snack.description
        db_snack.category = snack.category
        db_snack.recipe_id = snack.recipe.id if snack.recipe else None
        db_snack.snack_type = snack.snack_type
        db_snack.flavor_profile = snack.flavor_profile
        
        self.db.flush()
        self.db.refresh(db_snack)
        return db_snack
    
    def delete(self, snack_id: int) -> bool:
        """Elimina un snack por ID."""
        db_snack = self.db.query(SnackModel).get(snack_id)
        if db_snack:
            self.db.delete(db_snack)
            self.db.flush()
            return True
        return False
