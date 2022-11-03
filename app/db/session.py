from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.settings.core import core_settings

engine = create_engine(
    core_settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True, pool_recycle=3600
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
