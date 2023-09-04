from django.urls import path
from .views import CreateDonationView


urlpatterns = [
    path('', CreateDonationView.as_view(), name='create-donation'),
]
