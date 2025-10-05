from fastapi import APIRouter, Depends

from service.product_service import ProductService
from middleware.auth import get_current_user
from config.db import get_mongo

import models.product_model as product
import models.model as model

service = ProductService(get_mongo())
router = APIRouter(prefix="/products", tags=["products"])

@router.post("/create", dependencies=[Depends(get_current_user)])
def create(param: product.Product):
    return service.create_product(param)

@router.post("/get-all", dependencies=[Depends(get_current_user)])
def read_all(param: model.RPagination):
    return service.get_all_product(param)

@router.get("/{id}", dependencies=[Depends(get_current_user)])
def read_one(id: str):
    return service.get_product(id)

@router.put("/{id}", dependencies=[Depends(get_current_user)])
def read_one(id: str, param: product.Product):
    return service.update_product(id, param)

@router.delete("/{id}", dependencies=[Depends(get_current_user)])
def delete(id: str):
    return service.delete_product(id)