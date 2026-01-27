from typing import Optional
from datetime import datetime, timedelta
from src.domain.models.Employees import Employee
import holidays

class Shift:
    def __init__(self, id: Optional[int], employee: Employee, start_at: datetime, end_at: Optional[datetime], total_hours: Optional[float], is_active: bool, shift_payment_id: Optional[int]  = None):
        self.id = id
        self.employee = employee
        self.start_at = start_at # Nuestro turno comienza en esta fecha y hora actual.
        self.end_at = end_at 
        self.total_hours = total_hours
        self.is_active = is_active
        self.shift_payment_id = shift_payment_id # El ID del pago asociado a este turno, si existe. 

    @staticmethod
    def isHolidayOrSunday(datetime: datetime)-> bool:
        colombia_holydays = holidays.Colombia()
        date = datetime.date()
        if date.weekday() == 6 or date in colombia_holydays:
            return True
        return False
    
    @staticmethod
    def isNightHour(datetime:datetime)-> bool:
        hour = datetime.hour

        if hour >= 6 and hour < 7:
            return True
        return False

    def calculate_total_hours(self, initialDateTime: datetime, finalDateTime:datetime | None)-> float | None:
        if finalDateTime is not None:
            diferenceDate = finalDateTime - initialDateTime
            return diferenceDate.total_seconds() / 3600
        return None
    
    def hoursDistribution(self, startDate: datetime, endDate: datetime, total_hours: float) -> HourDistribution:
        hd = HourDistribution() 
        current = startDate

        if (total_hours > 8):
            hd.overtime_hours = total_hours - 8

        while current < endDate:

            next_block = min(current + timedelta(hours=1), endDate)

            # duración real del bloque (puede ser fracción)
            block_hours = (next_block - current).total_seconds() / 3600

            if self.isHolidayOrSunday(current):
                hd.sunday_holyday_hours += block_hours

            if self.isNightHour(current):
                hd.night_hours += block_hours
            else:
                hd.daytime_hours += block_hours

            current = next_block
            
        return hd
            

''' Represents a payment for one or more shifts. '''
class ShiftPayment:
    def __init__(self, id: Optional[int], shifts:list[Shift], payment_date: datetime, total_amount: float = 0.0):
        self.id = id
        self.shifts = shifts
        self.total_amount = total_amount
        self.payment_date = payment_date

    def calculate_total_amount(self, employeeSalary: int, hoursDistribution: list[HourDistribution])-> float:
        totalAmount = 0

        for i in hoursDistribution:
            totalAmount += (i.daytime_hours * employeeSalary) + (i.night_hours * (employeeSalary * 1.35)) + (i.sunday_holyday_hours * (employeeSalary * 1.75)) + (i.overtime_hours * employeeSalary)
        
        return totalAmount

class HourDistribution:
    def __init__(self):
        self.sunday_holyday_hours = 0
        self.daytime_hours = 0
        self.night_hours = 0
        self.overtime_hours = 0

