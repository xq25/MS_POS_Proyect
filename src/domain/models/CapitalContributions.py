from datetime import datetime
from typing import Optional

class CapitalContribution:
    def __init__(self, id: Optional[int], amount: float, date: datetime, description: Optional[str]):
        self.id = id
        self.amount = amount
        self.date = date
        self.description = description