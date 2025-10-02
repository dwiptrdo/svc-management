from fastapi import APIRouter, Depends, HTTPException
from config.db import get_mongo
from service.article_service import create_article, get_articles, get_article, delete_article

router = APIRouter(prefix="/articles", tags=["articles"])

@router.post("/create")
def create(title: str, content: str, mongo_db=Depends(get_mongo)):
    return create_article(mongo_db, title, content)

@router.get("/get-all")
def read_all(mongo_db=Depends(get_mongo)):
    return get_articles(mongo_db)

@router.get("/{article_id}")
def read_one(article_id: str, mongo_db=Depends(get_mongo)):
    article = get_article(mongo_db, article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@router.delete("/{article_id}")
def delete(article_id: str, mongo_db=Depends(get_mongo)):
    ok = delete_article(mongo_db, article_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Article not found")
    return {"message": "Deleted"}
