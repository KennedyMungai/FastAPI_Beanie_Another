"""The models script for the app"""
from datetime import datetime
from typing import Optional

from beanie import Document
from pydantic import BaseModel


class ProductReview(Document):
    """The ProductReview model"""
    name: str
    product: str
    rating: float
    review: str
    date: datetime = datetime.now()

    class Settings:
        """The settings for the ProductReview model"""
        name = "product_review"

    class Config:
        """The config for the ProductReview model"""
        schema_extra = {
            "example": {
                "name": "John",
                "product": "iPhone",
                "rating": 5.0,
                "review": "This is a good product",
                "date": datetime.now()
            }
        }


class UpdateProductReview(BaseModel):
    """The UpdateProductReview model"""
    name: Optional[str]
    product: Optional[str]
    rating: Optional[float]
    review: Optional[str]
    date: Optional[datetime]

    class Config:
        """The config for the UpdateProductReview model"""
        schema_extra = {
            "example": {
                "name": "John",
                "product": "iPhone",
                "rating": 5.0,
                "review": "This is a good product",
                "date": datetime.now()
            }
        }
