from src.infrastructure.db.repositories.product_repository_sqlalchemy import ProductRepositorySQLAlchemy
from src.domain.models.Products import (
    Product, Beer, Drink, Food, Cocktail, Shot, Snack,
    Category, BeerProfile, DrinkBases, FoodProfile, CocktailProfile, MainLiquor, SnackType, FlavorProfileSnacks
)
from src.domain.models.Recipes import Recipe
from src.infrastructure.db.models.productModel import ProductModel
from src.infrastructure.db.models.Products.beerModel import BeerModel
from src.infrastructure.db.models.Products.drinkModel import DrinkModel
from src.infrastructure.db.models.Products.foodModel import FoodModel
from src.infrastructure.db.models.Products.cocktailModel import CocktailModel
from src.infrastructure.db.models.Products.shotModel import ShotModel
from src.infrastructure.db.models.Products.snackModel import SnackModel
from typing import Optional, List, Union

class ProductService:

    def __init__(self, productRepo: ProductRepositorySQLAlchemy):
        self.repository = productRepo

    def getAll(self) -> List[Product]:
        db_products = self.repository.get_all()
        return [self._model_to_domain(db_product) for db_product in db_products]

    def getById(self, product_id: int) -> Optional[Product]:
        db_product = self.repository.get_by_id(product_id)
        return self._model_to_domain(db_product) if db_product else None

    def getByCategory(self, category: Category) -> List[Product]:
        db_products = self.repository.get_by_category(category)
        return [self._model_to_domain(db_product) for db_product in db_products]

    def create(self, product: Product) -> Product:
        db_product = self._domain_to_model(product)
        created = self.repository.create(db_product)
        return self._model_to_domain(created)

    def update(self, product_id: int, updated_product: Product) -> Optional[Product]:
        db_product = self._domain_to_model(updated_product)
        db_product.id = product_id
        updated = self.repository.update(db_product)
        return self._model_to_domain(updated) if updated else None

    def delete(self, product_id: int) -> bool:
        return self.repository.delete(product_id)

    def createProductFromData(self, data: dict) -> Product:
        category = data.get('category')
        if category == Category.BEER:
            return Beer(
                id=None,
                name=data['name'],
                price=data['price'],
                description=data['description'],
                category=category,
                recipe=data.get('recipe'),  # Asumir Recipe o None
                alcohol_percentage=data['alcohol_percentage'],
                profile=data['profile'],
                origin=data['origin'],
                is_national=data['is_national']
            )
        elif category == Category.DRINK:
            return Drink(
                id=None,
                name=data['name'],
                price=data['price'],
                description=data['description'],
                category=category,
                recipe=data.get('recipe'),
                is_alcoholic=data['is_alcoholic'],
                base=data['base'],
                is_hot=data['is_hot']
            )
        elif category == Category.FOOD:
            return Food(
                id=None,
                name=data['name'],
                price=data['price'],
                description=data['description'],
                category=category,
                recipe=data.get('recipe'),
                is_vegan=data['is_vegan'],
                for_sharing=data['for_sharing'],
                profile=data['profile']
            )
        elif category == Category.COCKTAIL:
            return Cocktail(
                id=None,
                name=data['name'],
                price=data['price'],
                description=data['description'],
                category=category,
                recipe=data.get('recipe'),
                profile=data['profile'],
                main_liquor=data['main_liquor']
            )
        elif category == Category.SNACK:
            return Snack(
                id=None,
                name=data['name'],
                price=data['price'],
                description=data['description'],
                category=category,
                recipe=data.get('recipe'),
                snack_type=data['snack_type'],
                flavor_profile=data['flavor_profile']
            )
        else:
            # Para Shot o base
            return Product(
                id=None,
                name=data['name'],
                price=data['price'],
                description=data['description'],
                category=category,
                recipe=data.get('recipe')
            )

    def _model_to_domain(self, db_product: ProductModel) -> Product:
        recipe = self._map_recipe(db_product.recipe) if db_product.recipe else None
        if isinstance(db_product, BeerModel):
            return Beer(
                id=db_product.id,
                name=db_product.name,
                price=db_product.price,
                description=db_product.description,
                category=db_product.category,
                recipe=recipe,
                alcohol_percentage=db_product.alcohol_percentage,
                profile=db_product.profile,
                origin=db_product.origin,
                is_national=db_product.is_national
            )
        elif isinstance(db_product, DrinkModel):
            return Drink(
                id=db_product.id,
                name=db_product.name,
                price=db_product.price,
                description=db_product.description,
                category=db_product.category,
                recipe=recipe,
                is_alcoholic=db_product.is_alcoholic,
                base=db_product.base,
                is_hot=db_product.is_hot
            )
        elif isinstance(db_product, FoodModel):
            return Food(
                id=db_product.id,
                name=db_product.name,
                price=db_product.price,
                description=db_product.description,
                category=db_product.category,
                recipe=recipe,
                is_vegan=db_product.is_vegan,
                for_sharing=db_product.for_sharing,
                profile=db_product.profile
            )
        elif isinstance(db_product, CocktailModel):
            return Cocktail(
                id=db_product.id,
                name=db_product.name,
                price=db_product.price,
                description=db_product.description,
                category=db_product.category,
                recipe=recipe,
                profile=db_product.profile,
                main_liquor=db_product.main_liquor
            )
        elif isinstance(db_product, ShotModel):
            return Shot(
                id=db_product.id,
                name=db_product.name,
                price=db_product.price,
                description=db_product.description,
                category=db_product.category,
                recipe=recipe,
                main_liquor=db_product.main_liquor
            )
        elif isinstance(db_product, SnackModel):
            return Snack(
                id=db_product.id,
                name=db_product.name,
                price=db_product.price,
                description=db_product.description,
                category=db_product.category,
                recipe=recipe,
                snack_type=db_product.snack_type,
                flavor_profile=db_product.flavor_profile
            )
        else:
            return Product(
                id=db_product.id,
                name=db_product.name,
                price=db_product.price,
                description=db_product.description,
                category=db_product.category,
                recipe=recipe
            )

    def _domain_to_model(self, product: Product) -> ProductModel:
        recipe_id = product.recipe.id if product.recipe else None
        if isinstance(product, Beer):
            return BeerModel(
                name=product.name,
                price=product.price,
                description=product.description,
                category=product.category,
                recipe_id=recipe_id,
                alcohol_percentage=product.alcohol_percentage,
                profile=product.profile,
                origin=product.origin,
                is_national=product.is_national
            )
        elif isinstance(product, Drink):
            return DrinkModel(
                name=product.name,
                price=product.price,
                description=product.description,
                category=product.category,
                recipe_id=recipe_id,
                is_alcoholic=product.is_alcoholic,
                base=product.base,
                is_hot=product.is_hot
            )
        elif isinstance(product, Food):
            return FoodModel(
                name=product.name,
                price=product.price,
                description=product.description,
                category=product.category,
                recipe_id=recipe_id,
                is_vegan=product.is_vegan,
                for_sharing=product.for_sharing,
                profile=product.profile
            )
        elif isinstance(product, Cocktail):
            return CocktailModel(
                name=product.name,
                price=product.price,
                description=product.description,
                category=product.category,
                recipe_id=recipe_id,
                profile=product.profile,
                main_liquor=product.main_liquor
            )
        elif isinstance(product, Shot):
            return ShotModel(
                name=product.name,
                price=product.price,
                description=product.description,
                category=product.category,
                recipe_id=recipe_id,
                main_liquor=product.main_liquor
            )
        elif isinstance(product, Snack):
            return SnackModel(
                name=product.name,
                price=product.price,
                description=product.description,
                category=product.category,
                recipe_id=recipe_id,
                snack_type=product.snack_type,
                flavor_profile=product.flavor_profile
            )
        else:
            return ProductModel(
                name=product.name,
                price=product.price,
                description=product.description,
                category=product.category,
                recipe_id=recipe_id,
                type="product"  # O determinar basado en category
            )

    def _map_recipe(self, db_recipe) -> Recipe:
        # Implementar mapeo completo si es necesario, por ahora simplificar
        return Recipe(
            id=db_recipe.id,
            name=db_recipe.name,
            ingredients=[],  # Mapear ingredients si necesario
            instructions=db_recipe.instructions,
            document_link=db_recipe.document_link
        )

    