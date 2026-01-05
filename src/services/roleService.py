from src.domain.models.Roles import Role
from src.infrastructure.db.repositories.role_repository_sqlalchemy import RoleRepositorySQLAlchemy

class RoleService:
    def __init__(self, roleRepo: RoleRepositorySQLAlchemy):
        self.repository = roleRepo

    def getAll(self):
        db_roles = self.repository.get_all()
        if not db_roles:
            return []
        return [
            Role(
                id=role.id, 
                name=role.name, 
                permissions= []
            ) 
            for role in db_roles]
    
    def getAllWithPermissions(self):
        db_roles = self.repository.get_all()
        if not db_roles:
            return []
        return [
            Role(
                id=role.id, 
                name=role.name, 
                permissions=[per.id for per in role.permissions]
            ) 
            for role in db_roles]
    
    def getById(self, id:int):
        db_role = self.repository.get_by_id(id)
        if not db_role:
            raise Exception(f"El rol con id {id} no existe")
        return Role(
                id=db_role.id, 
                name=db_role.name, 
                permissions=[]
            )
    
    def getByIdWithPermissions(self, id:int):
        db_role = self.repository.get_by_id_with_permissions(id)
        if not db_role:
            raise Exception(f"El rol con id {id} no existe")
        return Role(
                id=db_role.id, 
                name=db_role.name, 
                permissions=[per.id for per in db_role.permissions]
            )
    
    def getByEmployeeId(self, employee_id:int):
        db_roles = self.repository.get_by_employee_id(employee_id)
        if not db_roles:
            return []
        return [
            Role(
                id=role.id, 
                name=role.name, 
                permissions=[]
            ) 
            for role in db_roles]
    
    def create(self, role: Role):
        if role.id is not None:
            role.id = None # Verificar si eso esta bien
        db_role = self.repository.create(role)
        return role
        
    
    def update(self, roleUpdate: Role):
        db_role_update =  self.repository.update(roleUpdate)

        if not db_role_update:
            raise Exception(f"El rol con id {roleUpdate.id} no existe")
        
        return roleUpdate
    
    def delete(self, id:int):
        db_role_deleted =  self.repository.delete(id)
        if not db_role_deleted:
            raise Exception(f"El rol con id {id} no existe")
        return db_role_deleted