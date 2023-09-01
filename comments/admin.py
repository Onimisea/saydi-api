from django.contrib import admin
from .models import Comment  # Import the Comment model

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment', 'content', 'posted_at',)
    list_filter = ('content__type', 'posted_at',)
    search_fields = ('name', 'email', 'comment', 'content')
    ordering = ('-posted_at',)

# Register the Comment model with the custom admin class
admin.site.register(Comment, CommentAdmin)
