# Generated by Django 4.2.4 on 2023-08-31 14:47

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="VolunteeringApplication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("firstname", models.CharField(max_length=50)),
                ("lastname", models.CharField(max_length=50)),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female")], max_length=7
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("state", models.CharField(max_length=30)),
                (
                    "lga",
                    models.CharField(
                        max_length=30, verbose_name="Local Government Area"
                    ),
                ),
                ("zip", models.CharField(max_length=30, verbose_name="ZIP Code")),
                (
                    "areas_of_interest",
                    ckeditor_uploader.fields.RichTextUploadingField(),
                ),
                (
                    "professional_background",
                    ckeditor_uploader.fields.RichTextUploadingField(),
                ),
                (
                    "how_you_find_us",
                    models.CharField(
                        max_length=255, verbose_name="How did you find out about us?"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Volunteering Application",
                "verbose_name_plural": "Volunteering Applications",
            },
        ),
    ]
