from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from src.infrastructure.db.base import Base
from src.infrastructure.db.associations.employee_role_table import employee_role_table

class EmployeeModel(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(15), nullable=False)
    salary = Column(Float, nullable=False)

    roles = relationship(
        "RoleModel",
        secondary=employee_role_table,
        lazy="joined",
        back_populates="employees"
    )
    shifts = relationship(
        "ShiftModel",
        back_populates="employee"
    )
    orders = relationship(
        "OrderModel",
        back_populates="employee"
    )
