from middleware.auth import get_current_user, create_access_token
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import SessionLocal
from service import user_service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users", dependencies=[Depends(get_current_user)])
def list_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)

@router.get("/users/{user_id}", dependencies=[Depends(get_current_user)])
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    return user

@router.post("/users")
def create_user(username: str, password: str, db: Session = Depends(get_db)):
    return user_service.create_user(db, username, password)

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = user_service.login_user(db, username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Username atau password salah")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@router.put("/users/{user_id}", dependencies=[Depends(get_current_user)])
def update_user(user_id: int, username: str, db: Session = Depends(get_db)):
    user = user_service.update_user(db, user_id, username)
    if not user:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    return user

@router.delete("/users/{user_id}", dependencies=[Depends(get_current_user)])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    return {"message": "User berhasil dihapus"}
