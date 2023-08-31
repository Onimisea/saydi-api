from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class VolunteeringApplication(models.Model):
  GENDER_CHOICES = [
    ("male", "Male"),
    ("female", "Female"),
  ]

  firstname = models.CharField(max_length=50)
  lastname = models.CharField(max_length=50)
  gender = models.CharField(max_length=7, choices=GENDER_CHOICES)
  email = models.EmailField()
  state = models.CharField(max_length=30)
  lga = models.CharField(max_length=30, verbose_name="Local Government Area")
  zip = models.CharField(max_length=30, verbose_name="ZIP Code")
  areas_of_interest = RichTextUploadingField()
  professional_background = RichTextUploadingField()
  how_you_find_us = models.CharField(max_length=255, verbose_name="How did you find out about us?")
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.email}"

  class Meta:
        verbose_name = "Volunteering Application"
        verbose_name_plural = "Volunteering Applications"