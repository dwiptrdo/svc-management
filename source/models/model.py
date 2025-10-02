from typing import Optional, Any
from pydantic import BaseModel
from time import perf_counter

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

class ListOptions(BaseModel):
    path: str = "image"
    limit: Optional[int] = 100
    offset: Optional[int] = 0
    sort_column: Optional[str] = "name"
    sort_order: Optional[str] = "desc"

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