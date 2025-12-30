from datetime import datetime
from typing import Optional

class Provision:
    def __init__(self, id: Optional[int], items: list[ProvisionItem], total_cost: float, supplier_id:Optional[int], date:datetime):
        self.id = id
        self.total_cost = total_cost
        self.items = items
        self.supplier_id = supplier_id
        self.date = date

class ProvisionItem:
    def __init__(self, id:int, item_stock_id, add_stock: float):
        self.id = id
        self.item_stock_id = item_stock_id
        self.add_stock = add_stock