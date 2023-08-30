from django.contrib import admin
from .models import User

from django.db import models
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CustomCKEditorWidget(CKEditorUploadingWidget):
    def __init__(self, *args, **kwargs):
        kwargs['config'] = {
            'extraPlugins': 'cloudinary',
            # 'cloudinary_upload_preset': 'your_preset_name',  # Replace with your Cloudinary upload preset
        }
        super().__init__(*args, **kwargs)


class UserAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CustomCKEditorWidget},
    }
    search_fields = ['username', 'email']
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    ordering = ['id']  # Order by ID by default


admin.site.register(User, UserAdmin)
