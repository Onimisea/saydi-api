from django.urls import path
from .views import FetchAllContent

urlpatterns = [
    path('', FetchAllContent.as_view(), name='all-contents'),
    # Other URL patterns...
]
