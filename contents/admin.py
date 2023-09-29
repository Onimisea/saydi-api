from django.contrib import admin
from .models import Content
from ckeditor.widgets import CKEditorWidget
from django.db import models


class ContentAdmin(admin.ModelAdmin):
    list_display = ('type', 'title', 'published', 'updated')
    list_filter = ('type', 'published', 'location')
    search_fields = ('id', 'title', 'summary', 'slug', 'location')
    # Prepopulate slug based on title
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

    class Media:
        js = (
            # Include Cloudinary uploader script
            'https://upload-widget.cloudinary.com/global/all.js',
            # Include your CKEditor Cloudinary uploader plugin
            '../static/ckeditor/ckeditor/plugins/cloudinaryuploader/plugin.js',
        )


admin.site.register(Content, ContentAdmin)
