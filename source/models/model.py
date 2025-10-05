from pydantic import BaseModel, Field
from typing import Optional, Any
from time import perf_counter

import math

class Pagination(BaseModel):
    size: int
    totalPages: int
    totalElements: int

class MetaData(BaseModel):
    status: bool
    message: str
    timeExecution: str
    pagination: Optional[Pagination] = None

class ResponseWrapper(BaseModel):
    metaData: MetaData
    data: Any

class RPagination(BaseModel):
    search: str = Field(default=None)
    search_by: list = Field(default=[])
    orderBy: str = Field(default="createdAt")
    order: str = Field(default="desc")
    page: int = Field(default=1)
    size: int = Field(default=10)

def Response(
    data: Any,
    status: bool = True,
    message: str = "OK",
    start_time: float = 0,
    pagination: Optional[Pagination] = None,
) -> ResponseWrapper:
    elapsed = (perf_counter() - start_time) * 1000  # in milliseconds
    return ResponseWrapper(
        metaData=MetaData(
            status=status,
            message=message,
            timeExecution=f"{elapsed:.6f}ms",
            pagination=pagination
        ),
        data=data
    )

def build_pagination(param: RPagination, total_elements: int) -> Pagination:
    size = max(1, param.size)  # biar gak 0
    total_pages = math.ceil(total_elements / size) if total_elements else 0
    return Pagination(
        size=size,
        totalPages=total_pages,
        totalElements=total_elements
    )