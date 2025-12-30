from sqlalchemy import Table, Column, Integer, ForeignKey
from src.infrastructure.db.base import Base

employee_role_table = Table(
    "employee_roles",
    Base.metadata,
    Column("employee_id", ForeignKey("employees.id"), primary_key=True),
    Column("role_id", ForeignKey("roles.id"), primary_key=True),
)
