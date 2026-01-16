from typing import Optional

class Employee:
    def __init__(self, id: Optional[int], name: str, email: str, phone: str, roles: list[int], salary:float):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.roles = roles
        self.salary = salary