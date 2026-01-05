from typing import Optional
class Role:
    def __init__(self, id: Optional[int], name: str, permissions: list[int]):
        self.id = id
        self.name = name
        self.permissions = permissions