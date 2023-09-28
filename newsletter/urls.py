from django.urls import path
from .views import NewsletterSubscriptionView

urlpatterns = [
    path('', NewsletterSubscriptionView.as_view(), name='subscribe'),
    # Other URL patterns...
]
