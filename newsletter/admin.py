from django.contrib import admin
from .models import NewsletterSubscription

# Register your models here.

class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at', 'is_subscribed')
    list_filter = ('is_subscribed',)
    search_fields = ('email',)
    ordering = ('-subscribed_at',)

admin.site.register(NewsletterSubscription, NewsletterSubscriptionAdmin)
