from typing import Optional
from src.domain.models.Recipes import Recipe
from enum import Enum

''' Base Product class '''
class Product:
    def __init__(self, id: Optional[int], name: str, price: float, description: str, category: Category, recipe: Optional[Recipe]):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.category = category
        self.recipe = recipe

''' Enum definitions for various product attributes '''
#  Categories of products
class Category(Enum):
    BEER = "cerveza"
    DRINK = "bebida"
    COCKTAIL = "coctel"
    FOOD = "comida"
    SNACK = "snack"
#  Bases for drinks
class DrinkBases(Enum):
    LEMONADE = "limonada"
    SODA = "soda"
    TONIC = "tonica"
    MILK = "leche"
    COFFEE = "cafe"
    WATER = "agua"
    WINE = "vino"
#  Flavor profiles for food items
class FoodProfile(Enum):
    SWEET = "dulce"
    SALTY = "salada"
    BITTERSWEET = "agridulce"
    ACID = "acida"
    SPICY = "picante"
#  Beer profiles
class BeerProfile(Enum):
    GOLDEN = "dorada"
    DARK = "oscura"
    RED = "roja"
    GREEN = "verde"
#  Cocktail profiles
class CocktailProfile(Enum):
    SWEET = "dulce"
    CITRIC = "citrico"
    DRY = "seco"
    HERBAL = "herbal"
    FRUITY = "frutal"
    BITTER = "amargo"
#  Main liquors used in cocktails
class MainLiquor(Enum):
    VODKA = "vodka"
    GIN = "ginebra"
    WHISKY = "whisky"
    RUM = "ron"
    JAGGER = "jagger"
    TEQUILA = "tequila"
    WINE = "vino"
    BRANDY = "brandy"
    SAKE = "sake"
    VERMOUTH = "vermut"
    MEZCAL = "mezcal"
    PISCO = "pisco"
    AMARETTO = "amaretto"
    COFFEE = "cafe"
    SMIRNOFF = "smirnoff"
#  Types of snacks
class SnackType(Enum):
    DESSERT = "postre"
    PASTRY = "pasteleria"
    BAKERY = "panaderia"
    SWEET = "dulce"
#  Flavor profiles for snacks
class FlavorProfileSnacks(Enum):
    SWEET = "dulce"
    SALTY = "salado"
    BITTERSWEET = "agridulce"
    SPICY = "picante"

# Product subclasses for specific product types

class Drink(Product):
    def __init__(self, id: Optional[int], name: str, price: float, description: str, category: Category, recipe: Recipe, is_alcoholic:bool, base: DrinkBases, is_hot: bool):
        super().__init__(id, name, price, description, category, recipe)
        self.is_alcoholic = is_alcoholic
        self.base = base
        self.is_hot = is_hot

class Food(Product):
    def __init__(self,id: Optional[int],name: str,price: float,description: str,category: Category,recipe: Recipe,is_vegan: bool,for_sharing: bool,profile: FoodProfile):
        super().__init__(id, name, price, description, category, recipe)
        self.is_vegan = is_vegan
        self.for_sharing = for_sharing
        self.profile = profile

class Beer(Product):
    def __init__(self,id: Optional[int],name: str,price: float,description: str,category: Category,recipe: Recipe,alcohol_percentage: float,profile: BeerProfile,origin: str,is_national: bool):
        super().__init__(id, name, price, description, category, recipe)
        self.alcohol_percentage = alcohol_percentage
        self.profile = profile
        self.origin = origin
        self.is_national = is_national

class Cocktail(Product):
    def __init__(self,id: Optional[int],name: str,price: float,description: str,category: Category,recipe: Recipe,profile: CocktailProfile,main_liquor: MainLiquor):
        super().__init__(id, name, price, description, category, recipe)
        self.profile = profile
        self.main_liquor = main_liquor

class Shot(Product):
    def __init__(self,id: Optional[int],name: str,price: float,description: str,category: Category,recipe: Recipe, main_liquor: MainLiquor):
        super().__init__(id, name, price, description, category, recipe)
        self.main_liquor = main_liquor

class Snack(Product):
    def __init__(self,id: Optional[int],name: str,price: float,description: str,category: Category, recipe: Recipe,snack_type: SnackType,flavor_profile: FlavorProfileSnacks):
        super().__init__(id, name, price, description, category, recipe)
        self.snack_type = snack_type
        self.flavor_profile = flavor_profile
