from sqlalchemy.orm import Session, joinedload
from src.infrastructure.db.models.permissionModel import PermissionModel
from src.domain.models.Permissions import Permission

class PermissionRepositorySQLAlchemy:
    def __init__(self, db: Session ):
        self.db = db

    def get_all(self):
        return self.db.query(PermissionModel).all()
    
    def get_by_id(self, permission_id):
        db_permission = (
            self.db.query(PermissionModel)
            .filter(PermissionModel.id == permission_id)
            .first()
        )
        if db_permission:
            return db_permission
        return None
    
    def get_by_role_id(self, role_id: int):
        return (
            self.db.query(PermissionModel)
            .join(PermissionModel.roles)
            .filter_by(id=role_id)
            .all()
        )
    
    def create(self, permission: Permission):
        db_permission = PermissionModel(
            name = permission.name,
            code = permission.code,
            description = permission.description
        )
        self.db.add(db_permission)
        return db_permission
    
    def update(self, permission: Permission):
        db_permission = self.db.query(PermissionModel).get(permission.id)
        if not db_permission:
            return None
        db_permission.name = permission.name
        db_permission.code = permission.code
        db_permission.description = permission.description
        self.db.add(db_permission)
        return db_permission
    
    def delete(self, permission_id: int):
        db_permission_deleted = self.db.query(PermissionModel).get(permission_id)
        if not db_permission_deleted:
            return None
        self.db.delete(db_permission_deleted)
        return db_permission_deleted