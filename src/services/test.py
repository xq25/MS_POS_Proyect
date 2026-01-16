from src.infrastructure.db.repositories.employee_repository_sqlalchemy import EmployeeRepositorySQLAlchemy
from src.infrastructure.db.repositories.role_repository_sqlalchemy import RoleRepositorySQLAlchemy
from src.services.employeeService import EmployeeService
from src.services.roleService import  RoleService
from src.services.permissionService import PermissionService
from src.infrastructure.db.repositories.permission_repository_sqlachemy import PermissionRepositorySQLAlchemy
from src.infrastructure.db.database import get_db
from src.domain.models.Employees import Employee
from src.domain.models.Roles import Role
from src.domain.models.Permissions import Permission

def test():
    jacobo = Employee(
        id=None,
        name='Jacobo Quintero',
        email='jacoboq92@gmail.com',
        phone= '3007177370',
        roles=[1],
        salary=7400
    )
    role1 = Role(
        id=None,
        name='admin',
        permissions=[1]
    )
    permission1 = Permission(
        id=None,
        code='update:products',
        description='actualizar productos'
    )

    # Obtener sesión de base de datos
    db = next(get_db())
    
    # # Crear repositorio y servicio con la sesión
    # permission_repo = PermissionRepositorySQLAlchemy(db)
    # permission_service = PermissionService(permission_repo)
    
    role_repo = RoleRepositorySQLAlchemy(db)
    role_service = RoleService(role_repo)

    employee_repo = EmployeeRepositorySQLAlchemy(db)
    employee_service = EmployeeService(employee_repo)

    # permisoCreado = permission_service.create(permission1)
    # roleCreado = role_service.create(role1)
    # employeeCreado = employee_service.createEmployee(jacobo)
    # get_employee = employee_service.getById(1)
    # Confirmar cambios en la base de datos
    db.commit()
    # print('Permiso creado')
    print('role creado')


test()