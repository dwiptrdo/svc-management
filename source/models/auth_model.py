from pydantic import BaseModel
from typing import Optional

class Auth(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None
    token: Optional[str] = None