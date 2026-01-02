from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.infrastructure.db.config import DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    echo=True  # poner en False en producción
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
