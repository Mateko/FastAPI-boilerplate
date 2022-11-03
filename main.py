from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.settings.core import core_settings
from app.api.api_v1.api import api_router

from starlette.middleware.cors import CORSMiddleware

app = FastAPI(title=core_settings.PROJECT_NAME, descirpiton=core_settings.DESCRIPTION)
app.mount("/static", StaticFiles(directory="app/static"), name="static")


if core_settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=core_settings.API_V1_STR)
