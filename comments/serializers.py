from rest_framework import serializers
from .models import Comment  # Import the Comment model
from contents.models import Content 

class CommentCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    comment = serializers.CharField()
    content_id = serializers.IntegerField()  # This field will store the content's ID

    def create(self, validated_data):
        # Extract the content_id from validated_data
        content_id = validated_data.pop('content_id')

        # Retrieve the Content object using the content_id
        content = Content.objects.get(pk=content_id)

        # Create and return a new Comment instance
        return Comment.objects.create(content=content, **validated_data)
