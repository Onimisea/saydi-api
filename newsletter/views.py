from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NewsletterSubscriptionSerializer

class NewsletterSubscriptionView(APIView):
    
    def post(self, request, format=None):
        serializer = NewsletterSubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Email subscription successful", "email": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"error": "Email subscription failed", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
