from fastapi import FastAPI
from .config import get_settings

settings = get_settings()

api = FastAPI(title=settings.app_name)

@api.get('/')
def root():
    return 'Hello from api'