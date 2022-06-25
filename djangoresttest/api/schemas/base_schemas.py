from datetime import datetime
from typing import Generic, Optional

from django.conf import settings
from django.core.paginator import Paginator
from django.db.models import QuerySet
from django.http import HttpRequest
from ninja.schema import Schema
from pydantic.generics import GenericModel

from djangoresttest.api.types.types import T


def to_camel(string: str) -> str:
    return "".join(word.capitalize() for word in string.split("_"))


class BaseSchema(Schema):
    creation_datetime: datetime
    deletion_datetime: Optional[datetime]


class Response(Schema, GenericModel, Generic[T]):
    ok: bool = True
    description: str = "OK"
    status_code: int
    data: Optional[T]

    class Config:
        arbitrary_types_allowed = True


class PaginatedResponse(Schema, GenericModel, Generic[T]):
    ok: bool = True
    description: str = "OK"
    status_code: int
    items: Optional[T]
    total_items: Optional[int]
    total_pages: Optional[int]
    has_next_page: Optional[bool]
    has_previous_page: Optional[bool]
    current_page: Optional[int]

    def paginate(self, queryset: QuerySet, request: HttpRequest):
        page_number: str = request.GET.get("page", "1")
        quantity_per_page: str = request.GET.get("quantity_per_page", str(settings.PAGINATOR_QUANTITY_PER_PAGE))
        paginator = Paginator(queryset, quantity_per_page)
        page = paginator.page(page_number)
        self.status_code = 200
        self.total_items = paginator.count
        self.total_pages = paginator.num_pages
        self.has_next_page = page.has_next()
        self.has_previous_page = page.has_previous()
        self.current_page = page.number
        self.items = page.object_list  # type: ignore
