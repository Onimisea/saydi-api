from django.contrib import admin
from .models import JobPosting

# Register your models here.

class JobPostingAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'application_deadline', 'created_at', 'slug')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('company', 'location', 'application_deadline')
    search_fields = ('title', 'company', 'location')
    ordering = ('-created_at', 'application_deadline')

admin.site.register(JobPosting, JobPostingAdmin)
