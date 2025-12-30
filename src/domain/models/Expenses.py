from datetime import datetime
from typing import Optional

class Expense: 
    def __init__(self, id: Optional[int], amount: float, type: ExpenseTypes, expense_date: datetime, description: Optional[str]):
        self.id = id
        self.amount = amount
        self.type = type
        self.expense_date = expense_date
        self.description = description
class ExpenseTypes:
    # RENT = "Renta"
    # UTILITIES = "Utilidades"
    SALARIES = "Salarios"
    # MAINTENANCE = "Mantenimiento"
    SUPPLIES = "Suministros"