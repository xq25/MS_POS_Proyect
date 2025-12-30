from sqlalchemy import Table, Column, Integer, ForeignKey
from src.infrastructure.db.base import Base

role_permission_table = Table(
    "role_permissions",
    Base.metadata,
    Column("role_id", ForeignKey("roles.id"), primary_key=True),
    Column("permission_id", ForeignKey("permissions.id"), primary_key=True),
)
