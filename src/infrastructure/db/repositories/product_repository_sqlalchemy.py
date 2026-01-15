from sqlalchemy.orm import Session
from src.infrastructure.db.models.productModel import ProductModel
from src.domain.models.Products import Product, Category

class ProductRepositorySQLAlchemy:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self)-> list[ProductModel]:
        return self.db.query(ProductModel).all()

    def get_by_id(self, product_id:int)->ProductModel | None:
        db_product = self.db.query(ProductModel).filter(ProductModel.id == product_id).first()

        if not db_product:
            return None
        return db_product
    
    def get_by_category(self, category: Category)->list[ProductModel]:
        db_products = self.db.query(ProductModel).filter(ProductModel.category == category).all()

        if not db_products:
            return []
        return db_products

    def create(self, db_product: ProductModel) -> ProductModel:
        self.db.add(db_product)
        self.db.flush()
        self.db.refresh(db_product)
        return db_product

    def update(self, db_product: ProductModel) -> ProductModel | None:
        existing = self.db.query(ProductModel).filter(ProductModel.id == db_product.id).first()
        if not existing:
            return None
        # Actualizar campos
        for key, value in db_product.__dict__.items():
            if not key.startswith('_'):
                setattr(existing, key, value)
        self.db.flush()
        self.db.refresh(existing)
        return existing

    def delete(self, product_id: int) -> bool:
        db_product = self.get_by_id(product_id)
        if db_product:
            self.db.delete(db_product)
            self.db.flush()
            return True
        return False
    

