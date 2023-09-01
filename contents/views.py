from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import generics
from .models import Content
from .serializers import ContentSerializer
from django.shortcuts import get_object_or_404

# Create your views here.


class ContentListView(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class PressReleaseListView(generics.ListAPIView):
    queryset = Content.objects.filter(type='press_release')
    serializer_class = ContentSerializer

class PolicyBriefListView(generics.ListAPIView):
    queryset = Content.objects.filter(type='policy_brief')
    serializer_class = ContentSerializer

class BlogPostListView(generics.ListAPIView):
    queryset = Content.objects.filter(type='blog_post')
    serializer_class = ContentSerializer

class AnnualReportListView(generics.ListAPIView):
    queryset = Content.objects.filter(type='annual_report')
    serializer_class = ContentSerializer

class FinancialReportListView(generics.ListAPIView):
    queryset = Content.objects.filter(type='financial_report')
    serializer_class = ContentSerializer
