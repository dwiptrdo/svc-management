from fastapi import APIRouter

from service.auth_service import AuthService
from config.db import get_mongo

import models.auth_model as auth

service = AuthService(get_mongo())
router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login(param: auth.Auth):
    return service.login(param)

@router.post("/logout")
def logout(param: auth.Auth):
    return service.logout(param)