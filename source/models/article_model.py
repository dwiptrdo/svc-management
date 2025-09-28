# model/article_model.py
def get_article_collection(mongo_db):
    return mongo_db["articles"]
