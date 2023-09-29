"""The product review route"""
from fastapi import APIRouter, HTTPException
from beanie import PydanticObjectId
from typing import List
from models.models import ProductReview


product_reviews_router = APIRouter(
    prefix="/product_reviews",
    tags=["Product Reviews"]
)


@product_reviews_router.get("/")
async def retrieve_all_products():
    """Retrieve all products"""
    return await ProductReview.find_all().to_list()
