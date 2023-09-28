from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactUsSerializer


# Create your views here.

class ContactUsView(APIView):

    def post(self, request, format=None):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "success": "Contact form submission successful",
                "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(
            {
                "error": "Contact form submission failed",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
