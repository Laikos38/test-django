import traceback
from json import dumps

from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse

from djangoresttest.api.schemas.base_schemas import Response
from djangoresttest.api.utils.exceptions.base_exception import BaseException
from djangoresttest.api.utils.exceptions.not_found_exception import NotFoundException


def exception_handler(request, exc) -> HttpResponse:
    response = Response(ok=False, status_code=500, description="Error")
    if settings.DEBUG:
        response.data = f"{traceback.format_exc()}"
    if isinstance(exc, NotFoundException):
        response.description = exc.msg
        response.status_code = exc.status_code
        response.ok = exc.ok
        response.data = None
    elif isinstance(exc, BaseException):
        response.description = exc.msg
        response.status_code = exc.status_code
        response.ok = exc.ok
        response.data = None
    response_dict = response.dict()
    return HttpResponse(
        dumps(response_dict, cls=DjangoJSONEncoder),
        status=response.status_code,
        content_type="application/json",
    )
