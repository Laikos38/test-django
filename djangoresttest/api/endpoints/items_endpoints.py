from django.http import HttpRequest
from ninja import Router

from djangoresttest.api.schemas.base_schemas import Response
from djangoresttest.api.services.auth_service import ApiKey

router = Router(auth=ApiKey(), tags=["Items"])


@router.get("/dummy", response=Response[str], url_name="dummy")
def dummy(request: HttpRequest):
    """Dummy endpoint."""
    print("dummy")
    return Response(status_code=200, data="msg")
