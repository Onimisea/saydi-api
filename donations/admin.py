from django.contrib import admin
from .models import Donation

# Register your models here.


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',
                    'frequency', 'amount', 'paid', 'created_at', 'updated_at')
    list_filter = ('frequency', 'paid')
    search_fields = ('first_name', 'last_name',
                     'email', 'reference')
    ordering = ('-created_at',)

    
