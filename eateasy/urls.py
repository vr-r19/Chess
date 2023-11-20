
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path("api/v1/dateen/", include("dateen.urls")),
    path("api/news", include("news.urls")),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
