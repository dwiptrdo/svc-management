from fastapi import APIRouter, Depends

from middleware.auth import get_current_user
from service.user_service import UserService
from config.db import get_mongo

import models.user_model as user
import models.model as model

service = UserService(get_mongo())
router = APIRouter(prefix="/users", tags=["users"])

@router.post("/create", dependencies=[Depends(get_current_user)])
def Create_User(param: user.User):
    return service.create_user(param)

@router.post("/get-all", dependencies=[Depends(get_current_user)])
def Get_All_User(param: model.RPagination):
    return service.get_all_user(param)

@router.get("/{id}", dependencies=[Depends(get_current_user)])
def Get_User(id: str):
    return service.get_user(id)

@router.put("/{id}", dependencies=[Depends(get_current_user)])
def update_user(id: str, param: user.User):
    return service.update_user(id, param)

@router.delete("/{id}", dependencies=[Depends(get_current_user)])
def delete_user(id: str):
    return service.delete_user(id)
