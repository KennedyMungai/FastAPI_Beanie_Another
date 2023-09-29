"""The product review route"""
from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException

from models.models import ProductReview

product_reviews_router = APIRouter(
    prefix="/product_reviews",
    tags=["Product Reviews"]
)


@product_reviews_router.get("/")
async def retrieve_all_products() -> List[ProductReview]:
    """Retrieve all products"""
    return await ProductReview.find_all().to_list()


@product_reviews_router.post("/")
async def add_product_review(review: ProductReview) -> dict[str, str]:
    """The function endpoint for adding a product review"""
    await review.create()
    return {"message": "Review Added Successfully"}


@product_reviews_router.get("/{id}")
async def get_review_record(id: PydanticObjectId) -> ProductReview:
    """The function to retrieve a single product review record"""
    review = await ProductReview.get(id)
    return review
