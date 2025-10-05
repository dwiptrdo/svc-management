from pymongo import MongoClient

import config.env as env

mongo_client = MongoClient(env.MONGO_URL)
mongo_db = mongo_client[env.MONGO_DB_NAME]

def get_mongo():
    return mongo_db
