from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# Create your models here.

class JobPosting(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = RichTextUploadingField()
    requirements = RichTextUploadingField()
    application_deadline = models.DateTimeField()
    featured_image = CloudinaryField(format="jpg", folder="JobPostingGraphics", verbose_name="Job Posting Graphic", default="")
    application_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "Job Post"
        verbose_name_plural = "Job Posts"
        ordering = ['-created_at']


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(JobPosting, self).save(*args, **kwargs)
