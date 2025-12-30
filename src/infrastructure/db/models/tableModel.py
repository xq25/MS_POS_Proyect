from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.infrastructure.db.base import Base


class TableModel(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    size = Column(Integer, nullable=False)

    # Relación: una mesa puede tener muchas órdenes a lo largo del tiempo, pero solo una activa a la vez
    orders = relationship(
        "OrderModel",
        back_populates="table"
    )
