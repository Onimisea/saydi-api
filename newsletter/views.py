from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NewsletterSubscriptionSerializer
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class NewsletterSubscriptionView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                # Other properties of your serializer
            }
        ),
        responses={200: 'Success', 400: 'Bad Request'}
    )
    def post(self, request, format=None):
        serializer = NewsletterSubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Email subscription successful", "email": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"error": "Email subscription failed", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
