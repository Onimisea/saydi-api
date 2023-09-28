from django.contrib import admin
from django.urls import path, include
from v1.views import welcome_view
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", welcome_view, name='homepage_welcome'),
    path("admin/", admin.site.urls),
    path("v1/", include("v1.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)