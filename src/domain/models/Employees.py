from typing import Optional
from src.domain.models.Roles import Role
from src.domain.models.Shifts import Shift


class Employee:
    def __init__(self, id: Optional[int], name: str, email: str, phone: str, roles: list[int], salary:float):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.roles = roles
        self.salary = salary