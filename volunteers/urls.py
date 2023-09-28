from django.urls import path
from .views import VolunteeringApplicationView

urlpatterns = [
    path('', VolunteeringApplicationView.as_view(), name='volunteering-application'),
    # Other URL patterns...
]
