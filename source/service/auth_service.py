from fastapi.responses import JSONResponse
from time import perf_counter

from middleware.auth import create_access_token

import models.auth_model as auth
import models.model as model
import utils.utils as util

class AuthService:
    def __init__(self, mongo_db):
        self.db = mongo_db

    def login(self, param: auth.Auth):
        start = perf_counter()

        try:
            col = self.db["users"]

            user = col.find_one({"email": param.email})
            if not user or not util.verify_password(param.password, user["password"]):
                return JSONResponse(
                    status_code=401,
                    content=model.Response(
                        data=None,
                        status=False,
                        message="Invalid email or password",
                        start_time=start
                    ).model_dump()
                )
            
            token = create_access_token({"user_id": user["_id"], "email": user["email"]})
            return model.Response(data={"access_token": token, "token_type": "bearer", "role": user["role"]}, start_time=start)
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
        
    def logout(self, param: auth.Auth):
        start = perf_counter()
        
        try:
            self.db["revoked_tokens"].insert_one({"token": param.token})

            return model.Response(
                data=None,
                message="Successfully logged out",
                start_time=start
            )
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
