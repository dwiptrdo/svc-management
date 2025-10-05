from fastapi import FastAPI
import config.env as env

from controller import user_controller, product_controller, auth_controller

app = FastAPI(
    root_path="/api/v1",
    title="Service Management API",
    description="API for managing users, products and authentication",
)

app.include_router(auth_controller.router)
app.include_router(user_controller.router)
app.include_router(product_controller.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(env.PORT))