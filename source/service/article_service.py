from bson import ObjectId
from models.article_model import get_article_collection

def create_article(mongo_db, title: str, content: str):
    col = get_article_collection(mongo_db)
    article = {"title": title, "content": content}
    result = col.insert_one(article)
    article["_id"] = str(result.inserted_id)
    return article

def get_articles(mongo_db):
    col = get_article_collection(mongo_db)
    return [
        {**doc, "_id": str(doc["_id"])}
        for doc in col.find()
    ]

def get_article(mongo_db, article_id: str):
    col = get_article_collection(mongo_db)
    doc = col.find_one({"_id": article_id})
    if doc:
        doc["_id"] = str(doc["_id"])
    return doc

def delete_article(mongo_db, article_id: str):
    col = get_article_collection(mongo_db)
    result = col.delete_one({"_id": ObjectId(article_id)})
    return result.deleted_count > 0
