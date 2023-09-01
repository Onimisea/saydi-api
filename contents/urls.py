from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContentListView.as_view(), name='content-list'),
    path('press-releases/', views.PressReleaseListView.as_view(), name='press-release-list'),
    path('policy-briefs/', views.PolicyBriefListView.as_view(), name='policy-brief-list'),
    path('blog-posts/', views.BlogPostListView.as_view(), name='blog-post-list'),
    path('annual-reports/', views.AnnualReportListView.as_view(), name='annual-report-list'),
    path('financial-reports/', views.FinancialReportListView.as_view(), name='financial-report-list'),
]
