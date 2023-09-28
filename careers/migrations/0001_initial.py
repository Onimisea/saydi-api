# Generated by Django 4.2.4 on 2023-08-31 13:40

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="JobPosting",
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
                ("title", models.CharField(max_length=200)),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=255, null=True, unique=True
                    ),
                ),
                ("company", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                ("description", ckeditor_uploader.fields.RichTextUploadingField()),
                ("requirements", ckeditor_uploader.fields.RichTextUploadingField()),
                ("application_deadline", models.DateTimeField()),
                ("application_url", models.URLField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Job Post",
                "verbose_name_plural": "Job Posts",
            },
        ),
    ]