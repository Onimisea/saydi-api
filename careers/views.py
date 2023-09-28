from django.shortcuts import render
from rest_framework import generics
from .models import JobPosting
from .serializers import JobPostingSerializer

# Create your views here.


class JobPostingListView(generics.ListAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
