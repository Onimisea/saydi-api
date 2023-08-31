from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class PolicyBrief(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    document = models.FileField(upload_to='policy_briefs/')
    published_date = models.DateField()

class PressRelease(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    published_date = models.DateField()

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    author = models.CharField(max_length=100)
    published_date = models.DateField()

class AnnualReport(models.Model):
    year = models.PositiveIntegerField()
    document = models.FileField(upload_to='annual_reports/')
    published_date = models.DateField()

class FinancialReport(models.Model):
    year = models.PositiveIntegerField()
    document = models.FileField(upload_to='financial_reports/')
    audit_date = models.DateField()
