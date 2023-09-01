from django.contrib import admin
from .models import Content

class ContentAdmin(admin.ModelAdmin):
    list_display = ('type', 'title', 'published', 'updated')
    list_filter = ('type', 'published', 'location')
    search_fields = ('id', 'title', 'summary', 'slug', 'location')
    prepopulated_fields = {'slug': ('title',)}  # Prepopulate slug based on title
    date_hierarchy = 'published'  # Enable date-based drilldown navigation

admin.site.register(Content, ContentAdmin)
