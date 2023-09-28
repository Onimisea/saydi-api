from rest_framework import serializers
from .models import Content
from comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class RelatedContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('title', 'slug', 'featured_image', 'published')

class ContentSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    related_contents = RelatedContentSerializer(many=True, read_only=True, source='get_related_contents')

    class Meta:
        model = Content
        fields = '__all__'