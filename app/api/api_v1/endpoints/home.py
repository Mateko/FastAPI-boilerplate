from fastapi import APIRouter, Request
from app.api.deps import template

router = APIRouter()


@router.get('/')
async def home(request: Request):
    return template("index.html", {"request": request})
