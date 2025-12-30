from typing import Optional
from src.domain.models.Orders import Order

class Table:
    def __init__(self, id: Optional[int], name: str, size: int, orders: Optional[list[Order]]):
        self.id = id
        self.name = name
        self.size = size
        self.orders = orders
       
