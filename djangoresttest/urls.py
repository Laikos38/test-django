from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView
from ninja import NinjaAPI

from djangoresttest.api.urls import router as api_v1_router
from djangoresttest.api.utils.exceptions.exception_handler import exception_handler

api = NinjaAPI(
    title="Django REST Test API",
    description="Simple REST API made with Django Ninja.",
    docs_url="/v1/docs",
)

api.add_router("v1/", api_v1_router)

urlpatterns = [
    path("api/", api.urls),
    path("", TemplateView.as_view(template_name="client/index.html")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # noqa


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# NinjaAPI exception handler
@api.exception_handler(Exception)
def raise_exception(request, exc: Exception):
    return exception_handler(request, exc)
