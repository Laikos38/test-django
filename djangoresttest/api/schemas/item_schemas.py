from ninja import Field, Schema
from pydantic import validator

from djangoresttest.api.schemas import BaseSchema


class ItemInSchema(Schema):
    name: str
    description: str
    attack: int
    defense: int
    magic: int

    @validator("attack", "defense", "magic")
    def min_max_value(cls, v):
        if v > 10 or v < -10:
            raise ValueError("Stats must be between -10 and 10.")
        return v


class ItemSchema(BaseSchema):
    name: str
    description: str
    owner_name: str = Field(None, alias="owner.username")
    attack: int
    defense: int
    magic: int
