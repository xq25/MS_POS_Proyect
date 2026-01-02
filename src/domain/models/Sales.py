from datetime import datetime
from enum import Enum
from src.domain.models.Orders import Order

class Sale:
    def __init__(self, sale_id:int, order: Order, payment_method: Payment_Method, recorded_at: datetime, IVA_rate: float = 0.19): # this IVA value is variable depending on the country and year
        self.sale_id = sale_id
        self.order = order
        self.total_amount = order.total_amount
        self.payment_method = payment_method
        self.recorded_at = recorded_at
        self.taxes = order.total_amount * IVA_rate
class Payment_Method(Enum):
    CREDIT_CARD = "Tarjeta de Credito"
    DEBIT_CARD = "Tarjeta de Debito"
    CASH = "Efectivo"
    BANK_TRANSFER = "Transferencia Bancaria"
        

