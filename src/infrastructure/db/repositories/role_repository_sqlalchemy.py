from src.infrastructure.db.models.roleModel import RoleModel
from sqlalchemy.orm import Session, joinedload
from src.domain.models.Roles import Role

class RoleRepositorySQLAlchemy:
    
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[RoleModel] | None:
        return self.db.query(RoleModel).all()
    
    def get_all_with_permissions(self) -> list[Role] | None:
        return self.db.query(RoleModel).options(joinedload(RoleModel.permissions)).all()
    
    def get_by_id(self, role_id) -> RoleModel:
        db_role = (
            self.db.query(RoleModel)
            .filter(RoleModel.id == role_id)
            .first()
        )
        return db_role
    
    def get_by_id_with_permissions(self, role_id) -> RoleModel | None:
        db_role =  (self.db.query(RoleModel)
                .options(joinedload(RoleModel.permissions))
                .filter(RoleModel.id == role_id)
                .first())
        return db_role
    
    def get_by_employee_id(self, employee_id) -> list[RoleModel] | None:
        roles = (
            self.db.query(RoleModel)
            .join(RoleModel.employees)
            .filter(RoleModel.employees.any(id=employee_id))
            .all()
        )
        return roles
    
    def create(self, role: Role) -> RoleModel:
        db_role = RoleModel(
            name = role.name
        )
        self.db.add(db_role)
        self.db.flush()
        
        # Asignar permisos si existen
        if role.permissions:
            from src.infrastructure.db.models.permissionModel import PermissionModel
            permissions = self.db.query(PermissionModel).filter(PermissionModel.id.in_(role.permissions)).all()
            db_role.permissions.extend(permissions)
        
        self.db.flush()
        self.db.refresh(db_role)
        return db_role
        
    def update(self, role: Role) -> RoleModel:
        db_role = self.db.query(RoleModel).get(role.id)

        if not db_role:
            return None
        
        db_role.name = role.name
        db_role.description = role.description
        
        # Actualizar permisos
        if role.permissions is not None:
            from src.infrastructure.db.models.permissionModel import PermissionModel
            permissions = self.db.query(PermissionModel).filter(PermissionModel.id.in_(role.permissions)).all()
            db_role.permissions = permissions
        
        self.db.flush()
        self.db.refresh(db_role)
        return db_role
    
    def delete(self, role_id: int) -> RoleModel:
        db_role = self.db.query(RoleModel).get(role_id)

        if not db_role:
            return None
            
        self.db.delete(db_role)
        self.db.flush()
        return db_role
