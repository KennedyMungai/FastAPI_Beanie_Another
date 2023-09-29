"""The main app in the backend application"""
from fastapi import FastAPI
from database.db import init_db
from routers.product_review import product_reviews_router

app = FastAPI(
    title="Beanie Rules",
    description="Some Dummy backend which has beanie as the ODM",
    version="0.10"
)


@app.on_event("startup")
async def start_db():
    """The call to initialize the database on startup"""
    await init_db()


@app.get(
    "/",
    tags=["Root"]
)
async def root() -> dict[str, str]:
    """The root endpoint for the application"""
    return {"message": "Hello World"}


app.include_router(product_reviews_router,
                   prefix="/product_reviews", tags=["Product Reviews"])
