from typing import Generator
from app.db.session import SessionLocal
from fastapi.templating import Jinja2Templates

template = Jinja2Templates(directory="app/templates").TemplateResponse


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
