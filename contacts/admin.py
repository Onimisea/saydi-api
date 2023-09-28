from django.contrib import admin
from .models import ContactUs
from django.db import models
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget()},
    }
    
    list_display = ('first_name', 'last_name', 'email', 'subject', 'sent_at')
    list_filter = ('sent_at',)
    search_fields = ('first_name', 'last_name', 'email', 'subject')
    ordering = ('-sent_at',)
