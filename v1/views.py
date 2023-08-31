# Create your views here.
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.http import JsonResponse

schema_view = get_schema_view(
    openapi.Info(
        title="SAYDi API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


def welcome_view(request):
    message = "Welcome to SAYDi"
    data = {"message": message}
    return JsonResponse(data)

