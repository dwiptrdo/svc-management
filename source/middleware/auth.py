from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, status
from datetime import datetime, timedelta
from jose import jwt, JWTError

from config.db import get_mongo

import config.env as env

security = HTTPBearer(auto_error=False)

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db=Depends(get_mongo)):
    print("DEBUG mode is off, verifying token...", env.DEBUG)
    if env.DEBUG == "true":
        return {"sub": "test-user", "role": "tester"}

    if not credentials:  # kalau token kosong
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated (no token provided)",
        )
    
    
    token = credentials.credentials
    
    if db["revoked_tokens"].find_one({"token": token}):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token revoked",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token invalid atau expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload

def create_access_token(data: dict, expires_delta: int = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta or int(env.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, env.SECRET_KEY, algorithm=env.ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, env.SECRET_KEY, algorithms=[env.ALGORITHM])
        return payload
    except JWTError:
        return None