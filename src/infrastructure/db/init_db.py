from src.infrastructure.db.base import Base
from src.infrastructure.db.database import engine

# IMPORTANTE: importar todos los modelos
from src.infrastructure.db.models import (
    capitalContributionModel,
    employeeModel,
    expenseModel,
    incomeModel,
    ingredientModel,
    invoiceModel,
    itemStockModel,
    orderModel,
    orderProductModel,
    permissionModel,
    productModel,
    provisionItemModel,
    provisionModel,
    recipeIngredientModel,
    recipeModel,
    roleModel,
    saleModel,
    shiftModel,
    shiftPaymentModel,
    supplierModel,
    tableModel,
    beerModel,
    cocktailModel,
    drinkModel,
    foodModel,
    shotModel,
    snackModel,
    employee_role_table,
    role_permission_table,
)

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()