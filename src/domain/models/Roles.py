from typing import Optional
from src.domain.models.Permissions import Permission
class Role:
    def __init__(self, id: Optional[int], name: str, permissions: list[Permission]):
        self.id = id
        self.name = name
        self.permissions = permissions