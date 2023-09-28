from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError


class Content(models.Model):
    CONTENT_TYPE_CHOICES = (
        ('press_release', 'Press Release'),
        ('policy_brief', 'Policy Brief'),
        ('blog_post', 'Blog Post'),
        ('annual_report', 'Annual Report'),
        ('financial_report', 'Financial Report'),
        # Add more type choices as needed
    )

    type = models.CharField(max_length=20, choices=CONTENT_TYPE_CHOICES)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255, null=True, blank=True)
    content = RichTextUploadingField()
    summary = RichTextUploadingField()
    location = models.CharField(max_length=100, null=True, blank=True)
    featured_image = CloudinaryField(
        format="jpg", folder="ContentFeaturedImages", verbose_name="Featured Image", null=True, blank=True)
    featured_document = CloudinaryField(
        resource_type="raw",  # Set resource_type to "raw" for non-image files
        format="pdf",  # Specify the desired format (in this case, PDF)
        folder="Reports",  # Set the folder where the PDFs will be stored
        verbose_name="PDF Report",
        blank=True
    )
    # download_link = models.URLField(null=True, blank=True)
    audit_date = models.DateTimeField(null=True, blank=True)
    published = models.DateTimeField()
    updated = models.DateTimeField(auto_now=True)

    def clean(self):
        # Check the content type and validate fields accordingly
        super().clean()

        if self.type == 'press_release':
            # Example: Press releases require a download link
            if not self.location:
                raise ValidationError("Location of press release is required.")
        elif self.type == 'annual_report' or self.type == 'financial_report':
            if not self.featured_document:
                raise ValidationError(
                    "Reports require a featured PDF document.")
        elif self.type == 'financial_report':
            if not self.audit_date:
                raise ValidationError(
                    "Financial Reports require an audit date")
        # Add similar checks for other content types

    def save(self, *args, **kwargs):
        # Generate a slug from the title if it's not provided
        if not self.slug:
            self.slug = slugify(self.title)
        super(Content, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.type}: {self.title} - {self.published}"

    def get_related_contents(self):
        # Retrieve related contents of the same type (excluding the current content)
        return Content.objects.filter(type=self.type).exclude(pk=self.pk)

    class Meta:
        ordering = ['-published']
