from pydantic import BaseSettings
from typing import List
from pydantic import AnyHttpUrl


class Settings(BaseSettings):
    API_V1_STR: str = ""
    PROJECT_NAME: str = "Boilerplate"
    DESCRIPTION: str = "Boilerplate app with fastapi and jinja2"

    MYSQL_SERVER: str = "default"
    MYSQL_USER: str = "default"
    MYSQL_PASSWORD: str = "default"
    MYSQL_DB: str = "default"

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:3000"]

    SQLALCHEMY_DATABASE_URI: str = (
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}"
    )


core_settings = Settings()
