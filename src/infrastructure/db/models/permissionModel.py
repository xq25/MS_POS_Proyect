
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.infrastructure.db.base import Base
from src.infrastructure.db.associations.role_permission_table import role_permission_table

class PermissionModel(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(100), unique=True, nullable=False)
    description = Column(String(255), nullable=True)

    roles = relationship(
        "RoleModel",
        secondary=role_permission_table,
        back_populates="permissions"
    )
