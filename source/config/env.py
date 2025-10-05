from dotenv import load_dotenv
import os

# Load .env hanya sekali di sini
load_dotenv()

# Ambil variable dari env
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
ALGORITHM = os.getenv("ALGORITHM")
SECRET_KEY = os.getenv("SECRET_KEY")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
MONGO_URL = os.getenv("MONGO_URL")
POSTGRES_URL = os.getenv("POSTGRES_URL")
PORT = os.getenv("PORT")
DEBUG = os.getenv("DEBUG")