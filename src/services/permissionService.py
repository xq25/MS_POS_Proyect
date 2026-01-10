from src.infrastructure.db.repositories.permission_repository_sqlachemy import PermissionRepositorySQLAlchemy
from src.domain.models.Permissions import Permission
class PermissionService:
    def __init__(self, permissionRepo: PermissionRepositorySQLAlchemy):
        self.repository = permissionRepo

    def getAll(self):
        db_permissions = self.repository.get_all()
        if not db_permissions:
            return []
        return [
            Permission(
                id=perm.id,
                code=perm.code,
                description=perm.description
            )
            for perm in db_permissions
        ]

    def getById(self, id:int):
        db_permission = self.repository.get_by_id(id)
        if not db_permission:
            raise Exception(f"El permiso con id {id} no existe")
        return Permission(
            id=db_permission.id,
            code=db_permission.code,
            description=db_permission.description
        )
    
    def getByRoleId(self, role_id:int):
        db_permissions = self.repository.get_by_role_id(role_id)
        if not db_permissions:
            return []
        return [
            Permission(
                id=perm.id,
                code=perm.code,
                description=perm.description
            )
            for perm in db_permissions
        ]
    def create(self, permission: Permission):
        if permission.id is not None:
            permission.id = None
        db_permission = self.repository.create(permission)
        return permission
    
    def update(self, permission: Permission):
        db_permission = self.repository.update(permission)
        if not db_permission:
            raise Exception(f"El permiso con id {permission.id} no existe")
        return permission
    
    def delete(self, id:int):
        db_permission_deleted = self.repository.delete(id)
        if not db_permission_deleted:
            raise Exception(f"El permiso con id {id} no existe")
        return db_permission_deleted