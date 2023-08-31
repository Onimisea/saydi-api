from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VolunteeringApplicationSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



# Create your views here.

class VolunteeringApplicationView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'firstname': openapi.Schema(type=openapi.TYPE_STRING),
                'lastname': openapi.Schema(type=openapi.TYPE_STRING),
                'gender': openapi.Schema(type=openapi.TYPE_STRING),
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                'state': openapi.Schema(type=openapi.TYPE_STRING),
                'lga': openapi.Schema(type=openapi.TYPE_STRING),
                'areas_of_interest': openapi.Schema(type=openapi.TYPE_STRING),
                'professional_background': openapi.Schema(type=openapi.TYPE_STRING),
                'how_you_find_us': openapi.Schema(type=openapi.TYPE_STRING),
                # Other properties of your serializer
            }
        ),
        responses={200: 'Success', 400: 'Bad Request'}
    )

    def post(self, request, format=None):
        serializer = VolunteeringApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "success": "Application submission successful",
                "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(
            {
                "error": "Application submission failed",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
