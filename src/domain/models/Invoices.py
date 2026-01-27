from datetime import datetime
from enum import Enum
from typing import Optional

class Invoice:
    def __init__(self, id: Optional[int], number: str, sale_id:int, total_amount: float, items: list[InvoiceItem], client_info: Client_Info | None, taxes: float, issued_at:datetime):
        self.id = id
        self.number = number
        self.sale_id = sale_id
        self.total_amount = total_amount
        self.items = items
        self.client_info = client_info
        self.taxes = taxes
        self.issued_at = issued_at

class InvoiceItem:
    def __init__(
        self,
        product_id:int,
        product_name: str,
        unit_price: float,
        quantity: int,
        total_price: float
    ):  
        self.product_id = product_id
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity = quantity
        self.total_price = total_price

'''this class represent client information with different document types cause is necessary to digital invoicing'''
class Client_Info:
    def __init__(self, id:str, name: str, email: str, doc_type: Document_Type):
        self.id = id # could be DNI, CEDULA  or similar
        self.name = name
        self.email = email
        self.doc_type = doc_type

class Document_Type(Enum):
    CEDULA_DE_CIUDADANIA = "CC"
    CEDULA_DE_EXTRANJERIA = "CE"
    PASAPORTE = "PP"