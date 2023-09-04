from django.urls import path
from .views import PaystackView

urlpatterns = [
    path('paystack/', PaystackView, name='paystack-webhook'),
    # Other URL patterns...
]
 