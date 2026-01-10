from src.domain.models.Employees import Employee
from src.domain.models.Roles import Role
from src.domain.models.Shifts import Shift
from src.infrastructure.db.repositories.employee_repository_sqlalchemy import EmployeeRepositorySQLAlchemy
class EmployeeService:
    '''EN CASO DE QUERER MIGGRAR A OTRO ORM O DB, SOLO CAMBIAR ESTA CAPA'''
    def __init__(self, employeeRepo: EmployeeRepositorySQLAlchemy):
        self.repository = employeeRepo

    def getAll(self)-> list[Employee] | list :
        db_employees = self.repository.get_all()
        if not db_employees:
            return []
        return [
            Employee(
                id=emp.id,
                name=emp.name,
                email=emp.email,
                phone=emp.phone,
                salary=emp.salary,
                roles = [role.id for role in emp.roles] if emp.roles else []
            )
            for emp in db_employees
        ]
    
    def getAllWithRoles(self):
        db_employees = self.repository.get_all_with_roles()
        if not db_employees:
            return []
        return [
            Employee(
                id=emp.id,
                name=emp.name,
                email=emp.email,
                phone=emp.phone,
                salary=emp.salary,
                roles = [role.id for role in emp.roles] if emp.roles else []
            )
            for emp in db_employees
        ]

    def getById(self, id:int)-> Employee:
        db_employee = self.repository.get_by_id(id)
        if not db_employee:
            raise Exception(f"Empleado con ID {id} no encontrado")
        return Employee(
            id=db_employee.id,
            name=db_employee.name,
            email=db_employee.email,
            phone=db_employee.phone,
            salary=db_employee.salary,     
            roles = []       
        )
    
    def getByIdWithRoles(self, id:int)-> Employee:
        db_employee = self.repository.get_by_id_with_roles(id)
        if not db_employee:
            raise Exception(f"Empleado con ID {id} no encontrado")
        return Employee(
            id=db_employee.id,
            name=db_employee.name,
            email=db_employee.email,
            phone=db_employee.phone,
            salary=db_employee.salary,
            roles = [role.id for role in db_employee.roles] if db_employee.roles else []
        )
    
    def getByEmail(self, email:str)-> Employee:
        db_employee = self.repository.get_by_email(email)
        if not db_employee:
            raise Exception(f"Empleado con email {email} no encontrado")
        return Employee(
            id=db_employee.id,
            name=db_employee.name,
            email=db_employee.email,
            phone=db_employee.phone,
            salary=db_employee.salary,
            roles = [role.id for role in db_employee.roles] if db_employee.roles else []
        )

    def createEmployee(self, employee: Employee):
        roles = employee.roles
        if employee.id is not None:
            employee.remove('id')
        if not roles:
            raise Exception("No se encontraron roles válidos")
        
        db_employee = self.repository.create(employee)
        db_employee.roles.extend(roles)

        return employee

    def update(self, employeeUpdate: Employee):
        return self.repository.update(employeeUpdate)

    def delete(self, id:int):
        db_employee_deleted =  self.repository.delete(id)
        if not db_employee_deleted:
            raise Exception(f"Empleado con ID {id} no encontrado")
        return db_employee_deleted