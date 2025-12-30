from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.infrastructure.db.base import Base
from src.infrastructure.db.associations.role_permission_table import role_permission_table

class RoleModel(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)

    permissions = relationship(
        "PermissionModel",
        secondary=role_permission_table,
        back_populates="roles"
    )
    employees = relationship(
        "EmployeeModel",
        secondary="employee_role_table",
        back_populates="roles"
    )
