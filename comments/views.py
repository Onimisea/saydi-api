from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CommentCreateSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CommentCreateView(APIView):
    @swagger_auto_schema(
        operation_description="Create a new comment.",
        request_body=CommentCreateSerializer,
        responses={
            201: openapi.Response(
                description="Comment created successfully",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="A success message indicating that the comment was posted successfully."
                        )
                    }
                )
            ),
            400: openapi.Response(
                description="Bad Request",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="A description of the error."
                        ),
                        'errors': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'field_name': openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(
                                        type=openapi.TYPE_STRING,
                                        description="A list of error messages for the field."
                                    ),
                                    description="Validation error messages for the fields with validation errors."
                                )
                            },
                            description="Validation error messages for specific fields."
                        )
                    }
                )
            )
        }
    )
    def post(self, request, format=None):
        serializer = CommentCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Comment was posted successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
