from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VolunteeringApplicationSerializer
from .models import VolunteeringApplication
import json


# Create your views here.

class VolunteeringApplicationView(APIView):
    
    def post(self, request, format=None):
        print(request.data)
        # Get the email address from the request data
        email = request.data.get('email')
        
        # Check if there is an existing application with the same email
        existing_application = VolunteeringApplication.objects.filter(email=email).first()
        
        if existing_application:
            return Response(
                {
                    "error": "You have already volunteered.",
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Convert the dictionary to a JSON string
        json_string = json.dumps(request.data)

        # Parse the JSON string back to a dictionary
        parsed_data = json.loads(json_string)


        # If there is no existing application, proceed with creating a new application
        serializer = VolunteeringApplicationSerializer(data=parsed_data)
        
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