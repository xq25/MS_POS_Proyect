from datetime import datetime
from typing import Optional

'''this class represent a relationship between products and orders at specific time 
esta clase es fundamental para mantener el historial de precios y cantidades en el momento de la orden a lo largo del tiempo'''
class Product_Order: 
    def __init__(self, product_id: int, quantity: int, price: float):
        self.product_id = product_id
        self.quantity = quantity
        self.price = price # price at the specific time of the order

class Order:
    def __init__(self, id:Optional[int], employee_id:int, table_id:int, products:list[Product_Order], total_amount:float, start_at: datetime, last_updated: Optional[datetime]=None):
        self.id = id
        self.employee_id = employee_id
        self.table_id = table_id
        self.products = products  # List of products with quantity and price at specific time
        self.total_amount = total_amount
        self.start_at = start_at
        self.last_updated = last_updated
