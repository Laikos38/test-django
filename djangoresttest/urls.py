from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("api/", include("djangoresttest.api.urls")),
    path("", TemplateView.as_view(template_name="client/index.html")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
