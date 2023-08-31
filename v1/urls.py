from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", welcome_view, name='welcome'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("newsletter/", include("newsletter.urls")),
    path("contacts/", include("contacts.urls")),
    path("volunteers/", include("volunteers.urls")),
]