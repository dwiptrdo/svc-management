from sqlalchemy.orm import Session
from models.user_model import User
from passlib.hash import bcrypt
import hashlib

def _normalize_password(password: str) -> str:
    """
    Bcrypt limit = 72 byte.
    Kalau password lebih panjang, pakai sha256 hexdigest dulu.
    """
    if len(password.encode("utf-8")) > 72:
        return hashlib.sha256(password.encode("utf-8")).hexdigest()
    return password

def hash_password(password: str) -> str:
    normalized = _normalize_password(password)
    return bcrypt.hash(normalized)

def verify_password(password: str, hashed: str) -> bool:
    normalized = _normalize_password(password)
    return bcrypt.verify(normalized, hashed)

def create_user(db: Session, username: str, password: str):
    print("PASWWWORD", password, username)
    hashed_pw = hash_password(password)
    user = User(username=username, password=hashed_pw)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user


def get_users(db: Session):
    return db.query(User).all()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, user_id: int, username: str):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.username = username
        db.commit()
        db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user
