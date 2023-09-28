from django.contrib import admin
from .models import VolunteeringApplication

# Register your models here.

class VolunteeringApplicationAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'gender', 'state', 'created_at', )
    list_filter = ('state', 'lga', 'gender', 'created_at')
    search_fields = ('firstname', 'lastname', 'email')
    ordering = ('-created_at',)

admin.site.register(VolunteeringApplication, VolunteeringApplicationAdmin)
