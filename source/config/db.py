from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from pymongo import MongoClient

import config.env as env

# ========== PostgreSQL ==========
# POSTGRES_URL = os.getenv("POSTGRES_URL", "postgresql://user:password@localhost:5432/mydb")

engine = create_engine(env.POSTGRES_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ========== MongoDB ==========
# MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/")
# MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "mydb")

mongo_client = MongoClient(env.MONGO_URL)
mongo_db = mongo_client[env.MONGO_DB_NAME]

def get_mongo():
    return mongo_db
