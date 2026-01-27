from sqlalchemy.orm import Session, joinedload
from src.domain.models.Shifts import Shift
from src.infrastructure.db.models.shiftModel import ShiftModel

class ShiftRepositorySQLAlchemy:
    def __init__(self, db:Session):
        self.db = db

    def get_all(self):
        return self.db.query(ShiftModel).all()
    
    def get_by_id_with_employee(self, shift_id:int) -> ShiftModel:
        db_shift = self.db.query(ShiftModel).options(joinedload(ShiftModel.employee)).filter(ShiftModel.id == shift_id).first()
        if not db_shift:
            return None
        return db_shift
    
    def get_all_by_employee_id(self, employee_id:int) -> list[ShiftModel]:
        db_shifts = self.db.query(ShiftModel).options(joinedload(ShiftModel.employee)).filter(ShiftModel.employee_id == employee_id).all()
        if not db_shifts:
            return []
        return db_shifts
    
    def get_all_by_employee_id_not_payment(self, employee_id:int)->list[ShiftModel] | list:
        db_shifts = self.db.query(ShiftModel).options(joinedload(ShiftModel.employee)).filter(
            ShiftModel.employee_id == employee_id,
            ShiftModel.shift_payment_id == None
        ).all()
        if not db_shifts:
            return []
        return db_shifts
    
    def get_not_payment(self)->list[ShiftModel] | list:
        db_shifts = self.db.query(ShiftModel).options(ShiftModel.employee).filter(ShiftModel.shift_payment_id == None).all()

        if not db_shifts:
            return []
        return db_shifts
    
    def create(self, shift: Shift)->ShiftModel:
        db_shift = ShiftModel(
            employee_id = shift.employee.id,
            start_at = shift.start_at,
            end_at = shift.end_at,
            total_hours = shift.total_hours,
            is_active = shift.is_active,
            shift_payment_id = shift.shift_payment_id
        )
        self.db.add(db_shift)
        self.db.flush()
        self.db.refresh(db_shift)
        return db_shift
    
    def update(self, shift:Shift):
        db_shift = self.get_by_id_with_employee(shift.id)
        if not db_shift:
            return None
        
        db_shift.employee_id = shift.employee.id
        db_shift.start_at = shift.start_at
        db_shift.end_at = shift.end_at
        db_shift.total_hours = shift.total_hours
        db_shift.is_active = shift.is_active
        db_shift.shift_payment_id = shift.shift_payment_id

        self.db.flush()
        self.db.refresh(db_shift)
        return db_shift
    
    def delete(self, shift_id:int)->ShiftModel:
        db_shift = self.db.query(ShiftModel).get(shift_id)

        if not db_shift:
            return None
        
        self.db.delete(db_shift)
        self.db.flush()
        
        return db_shift
    