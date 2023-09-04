from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", welcome_view, name='welcome'),
    path("newsletter/", include("newsletter.urls")),
    path("contacts/", include("contacts.urls")),
    path("volunteers/", include("volunteers.urls")),
    path("contents/", include("contents.urls")),
    path("comments/", include("comments.urls")),
    path("webhooks/", include("webhooks.urls")),
    path("donations/", include("donations.urls")),
    path("careers/", include("careers.urls")),
]
