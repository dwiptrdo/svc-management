from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    product_name: str
    category: str
    description: Optional[str] = None
    product_price: int
    stock_max: int
    stock_min: int
    status: Optional[str] = "inactive"
    image: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
