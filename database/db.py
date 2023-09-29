"""The database configuration file"""
from beanie import init_beanie
import motor.motor_asyncio
from models.models import ProductReview


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://localhost:27017/productreviews")

    await init_beanie(database=client.productreviews, document_models=[ProductReview])
