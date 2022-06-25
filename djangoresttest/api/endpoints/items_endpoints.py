from typing import List

from ninja import Router

from djangoresttest.api.schemas.base_schemas import PaginatedResponse, Response
from djangoresttest.api.schemas.item_schemas import ItemInSchema, ItemSchema
from djangoresttest.api.services import items_service
from djangoresttest.api.services.auth_service import ApiKey
from djangoresttest.api.types.types import AuthHttpRequest

router = Router(auth=ApiKey(), tags=["Items"])


@router.get("/", response=PaginatedResponse[List[ItemSchema]], url_name="get_all_user_items")
def get_all_user_items(request: AuthHttpRequest):
    """Get all current logged user items."""
    queryset = items_service.get_all_user_items(request.auth.id)
    response: PaginatedResponse = PaginatedResponse(status_code=200)
    response.paginate(queryset=queryset, request=request)
    return response


@router.post("/", response=Response[int], url_name="register_item")
def register_item(request: AuthHttpRequest, item_data: ItemInSchema):
    """Register a new item and returns the new item id."""
    return Response(data=items_service.register_item(item_data, request.auth.id), status_code=201)


@router.get("/{int:item_id}", response={200: Response[ItemSchema], 404: Response}, url_name="get_item_by")
def get_item_by(request: AuthHttpRequest, item_id: int):
    return Response(data=items_service.get_item_by_id(item_id, request.auth.id), status_code=200)


@router.delete("/{int:item_id}", response={200: Response[bool], 404: Response}, url_name="delete_item")
def delete_item(request: AuthHttpRequest, item_id: int):
    return Response(data=items_service.delete_item(item_id, request.auth.id), status_code=200)
