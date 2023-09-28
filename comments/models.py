from django.db import models
from contents.models import Content  # Import the Content model
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = RichTextUploadingField()
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='comments')  # Add the foreign key
    posted_at = models.DateTimeField(default=timezone.now)  # Add the created_at field

    def __str__(self):
        return f"{self.content.title} Comment by {self.name} ({self.email})"
    
    class Meta:
        ordering = ['-posted_at']
