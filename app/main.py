"""The main app in the backend application"""
from fastapi import FastAPI


app = FastAPI(
    title="Beanie Rules",
    description="Some Dummy backend which has beanie as the ODM",
    version="0.10"
)


@app.get(
    "/",
    tags=["Root"],
    title="Root",
    description="Root endpoint for the application",
    response_model=dict[str, str],
    response_model_exclude_unset=True
)
async def root() -> dict[str, str]:
    """The root endpoint for the application"""
    return {"message": "Hello World"}
