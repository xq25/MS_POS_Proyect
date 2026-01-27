from sqlalchemy.orm import Session
from src.infrastructure.db.models.Products.cocktailModel import CocktailModel
from src.domain.models.Products import Cocktail, CocktailProfile, MainLiquor
from src.infrastructure.db.repositories.product_repository_sqlalchemy import ProductRepositorySQLAlchemy

class CocktailRepositorySQLAlchemy(ProductRepositorySQLAlchemy):
    '''Repositorio específico para operaciones con cócteles.
    Los commits van en los controladores después de que todas las operaciones se hayan realizado con éxito.'''
    
    def __init__(self, db: Session):
        super().__init__(db)
        self.db = db

    def get_all(self) -> list[CocktailModel]:
        """Obtiene todos los cócteles."""
        return self.db.query(CocktailModel).all()
    
    def get_by_id(self, cocktail_id: int) -> CocktailModel | None:
        """Obtiene un cóctel por ID."""
        db_cocktail = self.db.query(CocktailModel).filter(CocktailModel.id == cocktail_id).first()
        return db_cocktail if db_cocktail else None
    
    def get_by_profile(self, profile: CocktailProfile) -> list[CocktailModel]:
        """Obtiene cócteles por perfil (dulce, cítrico, seco, herbal, frutal, amargo)."""
        db_cocktails = self.db.query(CocktailModel).filter(CocktailModel.profile == profile).all()
        return db_cocktails if db_cocktails else []
    
    def get_by_main_liquor(self, main_liquor: MainLiquor) -> list[CocktailModel]:
        """Obtiene cócteles por licor principal (vodka, ginebra, whisky, ron, tequila, etc)."""
        db_cocktails = self.db.query(CocktailModel).filter(CocktailModel.main_liquor == main_liquor).all()
        return db_cocktails if db_cocktails else []
    
    def get_sweet_cocktails(self) -> list[CocktailModel]:
        """Obtiene cócteles dulces."""
        db_cocktails = self.db.query(CocktailModel).filter(
            CocktailModel.profile == CocktailProfile.SWEET
        ).all()
        return db_cocktails if db_cocktails else []
    
    def get_fruity_cocktails(self) -> list[CocktailModel]:
        """Obtiene cócteles con perfil frutal."""
        db_cocktails = self.db.query(CocktailModel).filter(
            CocktailModel.profile == CocktailProfile.FRUITY
        ).all()
        return db_cocktails if db_cocktails else []
    
    def get_dry_cocktails(self) -> list[CocktailModel]:
        """Obtiene cócteles secos."""
        db_cocktails = self.db.query(CocktailModel).filter(
            CocktailModel.profile == CocktailProfile.DRY
        ).all()
        return db_cocktails if db_cocktails else []
    
    def get_herbal_cocktails(self) -> list[CocktailModel]:
        """Obtiene cócteles con perfil herbal."""
        db_cocktails = self.db.query(CocktailModel).filter(
            CocktailModel.profile == CocktailProfile.HERBAL
        ).all()
        return db_cocktails if db_cocktails else []
    
    def get_citric_cocktails(self) -> list[CocktailModel]:
        """Obtiene cócteles con perfil cítrico."""
        db_cocktails = self.db.query(CocktailModel).filter(
            CocktailModel.profile == CocktailProfile.CITRIC
        ).all()
        return db_cocktails if db_cocktails else []
    
    def get_by_profile_and_liquor(self, profile: CocktailProfile, main_liquor: MainLiquor) -> list[CocktailModel]:
        """Obtiene cócteles por perfil y licor principal combinados."""
        db_cocktails = self.db.query(CocktailModel).filter(
            CocktailModel.profile == profile,
            CocktailModel.main_liquor == main_liquor
        ).all()
        return db_cocktails if db_cocktails else []
    
    def create(self, cocktail: Cocktail) -> CocktailModel:
        """Crea un nuevo cóctel en la base de datos."""
        db_cocktail = CocktailModel(
            name=cocktail.name,
            price=cocktail.price,
            description=cocktail.description,
            category=cocktail.category,
            recipe_id=cocktail.recipe.id if cocktail.recipe else None,
            profile=cocktail.profile,
            main_liquor=cocktail.main_liquor
        )
        self.db.add(db_cocktail)
        self.db.flush()
        self.db.refresh(db_cocktail)
        return db_cocktail
    
    def update(self, cocktail: Cocktail) -> CocktailModel | None:
        """Actualiza un cóctel existente."""
        db_cocktail = self.db.query(CocktailModel).get(cocktail.id)
        if not db_cocktail:
            return None
        
        db_cocktail.name = cocktail.name
        db_cocktail.price = cocktail.price
        db_cocktail.description = cocktail.description
        db_cocktail.category = cocktail.category
        db_cocktail.recipe_id = cocktail.recipe.id if cocktail.recipe else None
        db_cocktail.profile = cocktail.profile
        db_cocktail.main_liquor = cocktail.main_liquor
        
        self.db.flush()
        self.db.refresh(db_cocktail)
        return db_cocktail
    
    def delete(self, cocktail_id: int) -> bool:
        """Elimina un cóctel por ID."""
        db_cocktail = self.db.query(CocktailModel).get(cocktail_id)
        if db_cocktail:
            self.db.delete(db_cocktail)
            self.db.flush()
            return db_cocktail
        return None
