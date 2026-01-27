from src.domain.models.Employees import Employee
from src.infrastructure.db.models.employeeModel import EmployeeModel
from src.infrastructure.db.repositories.employee_repository_sqlalchemy import EmployeeRepositorySQLAlchemy
class EmployeeService:
    def __init__(self, employeeRepo: EmployeeRepositorySQLAlchemy):
        self.repository = employeeRepo

    def db_to_domain(self, db_model: EmployeeModel) -> Employee:
        return Employee(
            id=db_model.id,
            name=db_model.name,
            email=db_model.email,
            phone=db_model.phone,
            roles = [r.id for r in db_model.roles] if db_model.roles else [],
            salary=db_model.salary 
        )

    def get_all(self) -> list[Employee] | list :
        db_employees = self.repository.get_all()

        if not db_employees:
            return []
        return [self.db_to_domain(e) for e in db_employees]
    
    def get_all_with_roles(self) -> list[Employee] | list:
        db_employees = self.repository.get_all_with_roles()

        if not db_employees:
            return []
        return [self.db_to_domain(e) for e in db_employees]

    def get_by_id(self, id:int) -> Employee:
        db_employee = self.repository.get_by_id(id)

        if not db_employee:
            raise Exception(f"Empleado con ID {id} no encontrado")
        return self.db_to_domain(db_employee)
    
    def get_by_id_with_roles(self, id:int) -> Employee:
        db_employee = self.repository.get_by_id_with_roles(id)

        if not db_employee:
            raise Exception(f"Empleado con ID {id} no encontrado")
        return self.db_to_domain(db_employee)
    
    def get_by_email(self, email:str) -> Employee:
        db_employee = self.repository.get_by_email(email)

        if not db_employee:
            raise Exception(f"Empleado con email {email} no encontrado")
        return self.db_to_domain(db_employee)

    def create(self, employee: Employee) -> Employee:
        roles = employee.roles

        if not roles:
            raise Exception("No se encontraron roles válidos")
        
        db_employee = self.repository.create(employee)
        return self.db_to_domain(db_employee)

    def update(self, employeeUpdate: Employee) -> Employee:
        db_employee_updated =  self.repository.update(employeeUpdate)
        
        if not db_employee_updated:
            raise ValueError(f'El empleado con id {employeeUpdate.id} no ha sido encontrado')
        
        return self.db_to_domain(db_employee_updated)

    def delete(self, id:int) -> Employee:
        db_employee_deleted =  self.repository.delete(id)

        if not db_employee_deleted:
            raise Exception(f"Empleado con ID {id} no encontrado")
        
        return self.db_to_domain(db_employee_deleted)
    