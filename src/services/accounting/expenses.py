from src.domain.models.Expenses import Expense

class ExpenseService:
    def __init__(self, expenseRepo: ExpenseRepositorySQLAlchemy):
        self.repository = expenseRepo
        
    def get_all(self) -> list[Expense]:
        pass