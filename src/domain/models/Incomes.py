from datetime import datetime
from typing import Optional

class Income: 
    def __init__ (self, id:Optional[int], total_day_amount:float, date: datetime, source: str = 'Ventas'):
        self.id = id
        self.total_day_amount = total_day_amount
        self.date = date
        self.source = source
