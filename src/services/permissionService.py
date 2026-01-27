from src.infrastructure.db.models.permissionModel import PermissionModel
from src.infrastructure.db.repositories.permission_repository_sqlachemy import PermissionRepositorySQLAlchemy
from src.domain.models.Permissions import Permission

class PermissionService:
    def __init__(self, permissionRepo: PermissionRepositorySQLAlchemy):
        self.repository = permissionRepo

    def db_to_domain(self, db_model: PermissionModel) -> Permission:
        return Permission(
            id = db_model.id,
            code = db_model.code,
            description=db_model.description
        )

    def get_all(self) -> list[Permission] | list:
        db_permissions = self.repository.get_all()

        if not db_permissions:
            return []
        return [self.db_to_domain(p) for p in db_permissions]

    def get_by_id(self, id:int) -> Permission:
        db_permission = self.repository.get_by_id(id)

        if not db_permission:
            raise Exception(f"El permiso con id {id} no existe")
        return self.db_to_domain(db_permission)
    
    def get_by_role_id(self, role_id:int) -> list[Permission] | list:
        db_permissions = self.repository.get_by_role_id(role_id)

        if not db_permissions:
            return []
        return [self.db_to_domain(p) for p in db_permissions]
    
    def create(self, permission: Permission) -> Permission:
        db_permission = self.repository.create(permission)

        return self.db_to_domain(db_permission)
    
    def update(self, permission: Permission) -> Permission:
        db_permission = self.repository.update(permission)

        if not db_permission:
            raise Exception(f"El permiso con id {permission.id} no existe")
        return self.db_to_domain(db_permission)
    
    def delete(self, id:int) -> Permission:
        db_permission_deleted = self.repository.delete(id)

        if not db_permission_deleted:
            raise Exception(f"El permiso con id {id} no existe")
        return self.db_to_domain(db_permission_deleted)