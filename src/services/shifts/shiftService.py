from src.domain.models.Employees import Employee
from src.domain.models.Shifts import Shift
from src.infrastructure.db.models.shiftModel import ShiftModel
from src.infrastructure.db.repositories.shifts.shift_repository_sqlalchemy import ShiftRepositorySQLAlchemy


class ShiftService:
    def __init__(self, shiftRepo: ShiftRepositorySQLAlchemy):
        self.repository = shiftRepo

    def db_to_domain(self, db_model:ShiftModel):
        return Shift(
            id=db_model.id,
            employee=Employee(
                id=db_model.employee_id,
                name=db_model.employee.name,
                email=db_model.employee.email,
                phone=db_model.employee.phone,
                roles=[],
                salary=db_model.employee.salary
            ),
            start_at=db_model.start_at,
            end_at=db_model.end_at,
            total_hours=db_model.total_hours,
            is_active=db_model.is_active,
            shift_payment_id=db_model.shift_payment_id
        )
        
    def getById(self, id:int):
        db_shift = self.repository.get_by_id_with_employee(id)
        if not db_shift:
            raise ValueError(f"El turno con id {id} no ha sido encontrado")
        return self.db_to_domain(db_shift)
    
    def getAllByEmployeeId(self, employee_id:int):
        db_shifts = self.repository.get_all_by_employee_id(employee_id)

        if len(db_shifts) > 0:
            return [self.db_to_domain(s) for s in db_shifts]
        else:
            return []
    
    def getAllNotPayment(self):
        db_shifts = self.repository.get_not_payment()

        if len(db_shifts) > 0:
            return [self.db_to_domain(s) for s in db_shifts]
        else:
            return []
        
    def getAllByEmployeeIdNotPayment(self, employee_id:int):
        db_shifts = self.repository.get_all_by_employee_id_not_payment(employee_id)

        if len(db_shifts) > 0:
            return [self.db_to_domain(s) for s in db_shifts]
        else:
            return []
        
    def create(self, shift: Shift):
        # Calculo explicito de las horas
        if shift.end_at:
            shift.total_hours = shift.calculate_total_hours(shift.start_at, shift.end_at)

        db_shift = self.repository.create(shift)
        return self.db_to_domain(db_shift)

    def update(self, shift: Shift):
        # Recalculacion de las horas de forma aislada

        if shift.end_at:
            shift.total_hours = shift.calculate_total_hours(shift.start_at, shift.end_at)

        db_shift = self.repository.update(shift)

        if not db_shift:
            raise ValueError(f'No se encontro el turno con id {shift.id}')
        return self.db_to_domain(db_shift)
    
    def delete(self, shift_id:int):
        db_shift = self.repository.delete(shift_id)

        if not db_shift:
            raise ValueError(f'No se encontro el turno con id {shift_id}')
        return self.db_to_domain(db_shift)

