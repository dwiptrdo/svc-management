from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    username: str
    password: str
    telephone: int
    email: str
    status: Optional[str] = Field(default="inactive")
    image: Optional[str] = None
    role: Optional[str] = Field(default="user")
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None

class User_v(BaseModel):
    class Config:
        populate_by_name = True
        extra = "ignore"

    id: str = Field(alias="_id")
    username: str
    telephone: int
    email: str
    status: Optional[str] = Field(default="inactive")
    image: Optional[str] = None
    role: Optional[str] = Field(default="user")
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
