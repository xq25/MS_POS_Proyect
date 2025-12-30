from typing import Optional

from src.domain.models.Sales import Sale

class Invoice:
    def __init__(self, id: Optional[int], number: str, sale:Sale, invoice_type:Invoice_Type, client_info: Client_Info):
        self.id = id
        self.number = number
        self.total_amount = sale.total_amount
        self.products = sale.order.products
        self.invoice_type = invoice_type
        self.client_info = client_info
        self.taxes = sale.taxes

class Invoice_Type:
    ELECTRONIC = "Factura Electronica"
    PAPER = "Factura Fisica"

'''this class represent client information with different document types cause is necessary to digital invoicing'''
class Client_Info:
    def __init__(self, id:str, name: str, email: str, doc_type: Document_Type):
        self.id = id # could be DNI, CEDULA  or similar
        self.name = name
        self.email = email
        self.doc_type = doc_type

class Document_Type:
    CEDULA_DE_CIUDADANIA = "CC"
    CEDULA_DE_EXTRANJERIA = "CE"
    PASAPORTE = "PP"