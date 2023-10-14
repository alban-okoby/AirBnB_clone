#!/usr/bin/python3
"""Define the Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review

    Attributes:
        place_id (str): The ID of the place
        user_id (str): The ID of the user
        text (str): The text of the review
    """
    place_id = ""
    user_id = ""
    text = ""
