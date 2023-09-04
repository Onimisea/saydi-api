from django.urls import path
from .views import JobPostingListView


urlpatterns = [
    path('', JobPostingListView.as_view(), name='job-postings'),
]