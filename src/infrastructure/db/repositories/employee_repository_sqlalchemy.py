from sqlalchemy.orm import Session, joinedload
from src.infrastructure.db.models.employeeModel import EmployeeModel
from src.domain.models.Employees import Employee

class EmployeeRepositorySQLAlchemy:
    '''Los commits van en los controladores despues de que todas las operaciones se hayan realizado con exito'''
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(EmployeeModel).all()
    
    def get_all_with_roles(self):
        return self.db.query(EmployeeModel).options(joinedload(EmployeeModel.roles)).all()
    
    def get_by_id(self, employee_id):
        db_employee = (
            self.db.query(EmployeeModel)
            .filter(EmployeeModel.id == employee_id)
            .first()
        )
        if db_employee:
            return db_employee
        return None
    
# Esta funcion sirve ccomo un contexto mas completo para ser usando en seguridad
    def get_by_id_with_roles(self, employee_id):
        db_employee = (
            self.db.query(EmployeeModel)
            .options(joinedload(EmployeeModel.roles))
            .filter(EmployeeModel.id == employee_id)
            .first()
        )
        if db_employee:
            return db_employee
        return None
    
    def get_by_email(self, email: str):
        db_employee = (
            self.db.query(EmployeeModel)
            .filter(EmployeeModel.email == email)
            .first()
        )
        if db_employee:
            return db_employee
        return None

    def create(self, employee: Employee):
        db_employee = EmployeeModel(
            name = employee.name,
            email = employee.email,
            phone = employee.phone,
            salary = employee.salary
        )
        self.db.add(db_employee)
        return db_employee

    def update(self, employee: Employee):
        db_employee = self.db.query(EmployeeModel).get(employee.id)
        if not db_employee:
            return None
        db_employee.name = employee.name
        db_employee.email = employee.email
        db_employee.phone = employee.phone
        db_employee.salary = employee.salary
        return db_employee

    def delete(self, employee_id: int):
        db_employee = self.db.query(EmployeeModel).get(employee_id)
        if db_employee:
            self.db.delete(db_employee)
            return db_employee
        return None