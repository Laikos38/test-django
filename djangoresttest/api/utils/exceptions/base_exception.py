import traceback
from json import dumps

from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse

from djangoresttest.api.schemas.base_schemas import Response


class BaseException(Exception):
    msg: str = "Error, please try again later."
    status_code: int = 500
    ok: bool = False

    def __init__(self, msg: str, status_code: int, ok: bool = False):
        self.msg = msg
        self.status_code = status_code
        self.ok = ok


def exception_handler(request, exc):
    response = Response(ok=False, status_code=500, description="Error")
    if settings.DEBUG:
        response.data = f"{traceback.format_exc()}"
    if isinstance(exc, BaseException):
        response.description = exc.msg
        response.status_code = exc.status_code
        response.ok = exc.ok
    response_dict = response.dict()
    return HttpResponse(
        dumps(response_dict, cls=DjangoJSONEncoder),
        status=response.status_code,
        content_type="application/json",
    )
