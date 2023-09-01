from django.urls import path
from .views import CommentCreateView  # Import the CommentCreateView


urlpatterns = [
    # Your other URL patterns go here
    path('create-comment/', CommentCreateView.as_view(), name='create-comment'),
]

