from fastapi.responses import JSONResponse
from time import perf_counter
from uuid import uuid4

import models.product_model as product
import models.model as model

class ProductService:
    def __init__(self, mongo_db):
        self.db = mongo_db

    def create_product(self, param: product.Product):
        start = perf_counter()

        try:
            col = self.db["product"]

            product_dict = param.model_dump()
            product_dict["_id"] = str(uuid4()).replace("-" , "")
            col.insert_one(product_dict)

            return model.Response(data={"id": product_dict["_id"]}, start_time=start)
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

    def get_all_product(self, param: model.RPagination):
        start = perf_counter()

        try:
            col = self.db["product"]

            query = {}
            if param.search and param.search_by:
                query["$or"] = [
                    {field: {"$regex": param.search, "$options": "i"}}
                    for field in param.search_by
                ]

            # sorting
            order = -1 if param.order.lower() == "desc" else 1
            skip = (param.page - 1) * param.size

            total_elements = col.count_documents(query)

            docs = col.find(query).sort(param.orderBy, order).skip(skip).limit(param.size)
            datas = [
                {**doc, "_id": str(doc["_id"])}
                for doc in docs
            ]

            return model.Response(data=datas, start_time=start, pagination=model.build_pagination(param, total_elements))
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

    def get_product(self, id: str):
        start = perf_counter()

        try:
            col = self.db["product"]
            doc = col.find_one({"_id": id})
            if not doc:
                return model.Response(data=None, status=False, message="Product not found", start_time=start)
            
            return model.Response(data=doc, start_time=start)
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
        
    def update_product(self, id: str, param: product.Product):
        start = perf_counter()

        try:
            col = self.db["product"]
            product_dict = param.model_dump()
            result = col.update_one({"_id": id}, {"$set": product_dict})
            if result.matched_count == 0:
                return model.Response(data=None, status=False, message="Product not found", start_time=start)

            return model.Response(data={"id": id}, message="Succesfully Update Product", start_time=start)
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

    def delete_product(self, id: str):
        start = perf_counter()

        try:
            col = self.db["product"]
            result = col.delete_one({"_id": id})
            if result.deleted_count == 0:
                return model.Response(data=None, status=False, message="Product not found", start_time=start)

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
