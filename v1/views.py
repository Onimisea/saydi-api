# Create your views here.
from rest_framework import permissions
from django.http import JsonResponse


def welcome_view(request):
    message = "Welcome to SAYDi"
    data = {"message": message}
    return JsonResponse(data)
