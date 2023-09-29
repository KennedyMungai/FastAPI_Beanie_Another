"""The main app in the backend application"""
from fastapi import FastAPI


app = FastAPI(
    title="Beanie Rules",
    description="Some Dummy backend which has beanie as the ODM",
    version="0.10"
)


@app.get(
    "/",
    tags=["Root"]
)
async def root() -> dict[str, str]:
    """The root endpoint for the application"""
    return {"message": "Hello World"}
