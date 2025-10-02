from sqlalchemy.orm import Session
from models.user_model import User

import utils.utils as util

def create_user(db: Session, username: str, password: str):
    print("PASWWWORD", password, username)
    hashed_pw = util.hash_password(password)
    user = User(username=username, password=hashed_pw)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def login_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return None
    if not util.verify_password(password, user.password):
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
