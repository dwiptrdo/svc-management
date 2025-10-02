from fastapi.responses import JSONResponse
from time import perf_counter
import models.model as model
from bson import ObjectId

def create_article(mongo_db, title: str, content: str):
    start = perf_counter()

    try:
        col = mongo_db["komputer"]
        article = {"title": title, "content": content}
        result = col.insert_one(article)
        article["_id"] = str(result.inserted_id)

        return model.Response(data=article, start_time=start)
    except Exception as e:
        return JSONResponse(
            status_code=422,
            content=model.Response(
                data=None,
                status=False,
                message=str(e),
                start_time=start
            ).model_dump()
        )

def get_articles(mongo_db):
    start = perf_counter()

    try:
        col = mongo_db["komputer"]
        datas = [
            {**doc, "_id": str(doc["_id"])}
            for doc in col.find()
        ]

        pagination = model.Pagination(
            size=1,
            totalPages=1,
            totalElements=len(datas)
        )
        return model.Response(data=datas, start_time=start, pagination=pagination)
    except Exception as e:
        return JSONResponse(
            status_code=422,
            content=model.Response(
                data=None,
                status=False,
                message=str(e),
                start_time=start
            ).model_dump()
        )

def get_article(mongo_db, article_id: str):
    start = perf_counter()

    try:
        col = mongo_db["komputer"]
        doc = col.find_one({"_id": ObjectId(article_id)})
        if doc:
            doc["_id"] = str(doc["_id"])
        
        pagination = model.Pagination(
            size=1,
            totalPages=1,
            totalElements=1
        )

        return model.Response(data=doc, start_time=start, pagination=pagination)
    except Exception as e:
        return JSONResponse(
            status_code=422,
            content=model.Response(
                data=None,
                status=False,
                message=str(e),
                start_time=start
            ).model_dump()
        )

def delete_article(mongo_db, article_id: str):
    start = perf_counter()

    try:
        col = mongo_db["komputer"]
        result = col.update_one(
            {"_id": ObjectId(article_id)},
            {"$set": {"is_deleted": True}}  # atau "status": False
        )

        return model.Response(data=None, start_time=start, message="Deleted Succesfully")
    except Exception as e:
        return JSONResponse(
            status_code=422,
            content=model.Response(
                data=None,
                status=False,
                message=str(e),
                start_time=start
            ).model_dump()
        )
