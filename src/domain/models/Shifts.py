from typing import Optional
from datetime import datetime
from src.domain.models.Employees import Employee

class Shift:
    def __init__(self, id: Optional[int], employee: Employee, start_at: datetime, end_at: Optional[datetime], is_active: bool, shift_payment_id: Optional[int]  = None):
        self.id = id
        self.employee = employee
        self.start_at = start_at # Nuestro turno comienza en esta fecha y hora actual.
        self.end_at = end_at 
        self.is_active = is_active
        self.shift_payment_id = shift_payment_id # El ID del pago asociado a este turno, si existe. 
        

''' Represents a payment for one or more shifts. '''
class ShiftPayment:
    def __init__(self, id: Optional[int], shifts:list[Shift], payment_date: datetime, amount: float):
        self.id = id
        self.shifts = shifts
        self.amount = amount
        self.payment_date = payment_date

