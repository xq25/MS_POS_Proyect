from src.domain.models.Roles import Role
from src.infrastructure.db.models.roleModel import RoleModel
from src.infrastructure.db.repositories.role_repository_sqlalchemy import RoleRepositorySQLAlchemy

class RoleService:
    def __init__(self, roleRepo: RoleRepositorySQLAlchemy):
        self.repository = roleRepo

    def db_to_domain(self, db_model: RoleModel) -> Role:
        return Role(
            id = db_model.id,
            name = db_model.name,
            permissions = [p.id for p in db_model.permissions] if db_model.permissions else []
        )

    def get_all(self) -> list[Role] | list:
        db_roles = self.repository.get_all()

        if not db_roles:
            return []
        return [self.db_to_domain(r) for r in db_roles]
    
    def get_all_with_permissions(self) -> list[Role] | list:
        db_roles = self.repository.get_all()

        if not db_roles:
            return []
        return [self.db_to_domain(r) for r in db_roles]
    
    def get_by_id(self, id:int) -> Role:
        db_role = self.repository.get_by_id(id)

        if not db_role:
            raise Exception(f"El rol con id {id} no existe")
        return self.db_to_domain(db_role)
    
    def get_by_id_with_permissions(self, id:int) -> Role:
        db_role = self.repository.get_by_id_with_permissions(id)

        if not db_role:
            raise Exception(f"El rol con id {id} no existe")
        return self.db_to_domain(db_role)
    
    def get_by_employee_id(self, employee_id:int) -> list[Role] | list:
        db_roles = self.repository.get_by_employee_id(employee_id)

        if not db_roles:
            return []
        return [self.db_to_domain(r) for r in db_roles]
    
    def create(self, role: Role) -> Role:
        if role.id is not None:
            role.id = None # Verificar si eso esta bien
        db_role = self.repository.create(role)

        return self.db_to_domain(db_role)
        
    def update(self, roleUpdate: Role) -> Role:
        db_role_update =  self.repository.update(roleUpdate)

        if not db_role_update:
            raise Exception(f"El rol con id {roleUpdate.id} no existe")
        return self.db_to_domain(db_role_update)
    
    def delete(self, id:int) -> Role:
        db_role_deleted =  self.repository.delete(id)
        if not db_role_deleted:
            raise Exception(f"El rol con id {id} no existe")
        return self.db_to_domain(db_role_deleted)
    