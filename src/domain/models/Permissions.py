from typing import Optional

class Permission:
    def __init__(self, id: Optional[int], code: str, description: str):
        self.id = id
        self.code = code # ejemplo: "Entidad:Accion".
        self.description = description