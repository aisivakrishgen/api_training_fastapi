from fastapi import APIRouter
from services.hello_service import get_greeting

router = APIRouter()

@router.get("/hello/{name}")
def say_hello(name: str):
    return get_greeting(name)
