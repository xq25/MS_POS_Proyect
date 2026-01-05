from src.infrastructure.db.models.roleModel import RoleModel
from sqlalchemy.orm import Session, joinedload
from src.domain.models.Roles import Role

class RoleRepositorySQLAlchemy:
    
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(RoleModel).all()
    
    def get_all_with_permissions(self):
        return self.db.query(RoleModel).options(joinedload(RoleModel.permissions)).all()
    
    def get_by_id(self, role_id):
        db_role = (
            self.db.query(RoleModel)
            .filter(RoleModel.id == role_id)
            .first()
        )
        return db_role
    
    def get_by_id_with_permissions(self, role_id):
        db_role =  (self.db.query(RoleModel)
                .options(joinedload(RoleModel.permissions))
                .filter(RoleModel.id == role_id)
                .first())
        return db_role
    
    def get_by_employee_id(self, employee_id):
        roles = (
            self.db.query(RoleModel)
            .join(RoleModel.employees)
            .filter(RoleModel.employees.any(id=employee_id))
            .all()
        )
        return roles
    
    def create(self, role: Role) -> Role:
        db_role = RoleModel(
            name = role.name,
            description = role.description
        )
        self.db.add(db_role)
        return db_role
        
    def update(self, role: Role):
        db_role = self.db.query(RoleModel).get(role.id)

        if not db_role:
            return None
        
        db_role.name = role.name
        db_role.description = role.description
        return db_role
    
    def delete(self, role_id: int):
        db_role = self.db.query(RoleModel).get(role_id)

        if db_role:
            self.db.delete(db_role)
            return db_role
        
        return None