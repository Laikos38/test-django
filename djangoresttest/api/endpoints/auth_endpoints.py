from django.http import HttpRequest
from ninja import Router

from djangoresttest.api.schemas.auth_schemas import LoginInSchema, TokenDataSchema
from djangoresttest.api.schemas.base_schemas import Response
from djangoresttest.api.services import auth_service

router = Router(tags=["Auth"])


@router.post("/login", response=Response[TokenDataSchema], url_name="login")
def login(request: HttpRequest, data: LoginInSchema):
    """Login / get api token."""
    token = TokenDataSchema(token=auth_service.authenticate_user(data))
    return Response(data=token, status_code=200)
