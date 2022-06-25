from ninja import Field, Schema

from djangoresttest.api.schemas import BaseSchema


class ItemInSchema(Schema):
    name: str
    description: str


class ItemSchema(BaseSchema):
    name: str
    description: str
    owner_name: str = Field(None, alias="owner.first_name")
