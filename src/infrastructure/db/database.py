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

def get_db():
    """Genera una sesión de base de datos y la cierra después"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
