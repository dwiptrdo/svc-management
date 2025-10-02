from controller import user_controller, article_controller
from config.db import Base, engine
from fastapi import FastAPI
import config.env as env

# create postgres tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_controller.router)
app.include_router(article_controller.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(env.PORT))