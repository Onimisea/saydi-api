# Generated by Django 4.2.4 on 2023-09-01 12:43

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contents", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="featured_document",
            field=cloudinary.models.CloudinaryField(
                blank=True, max_length=255, null=True, verbose_name="PDF Report"
            ),
        ),
        migrations.AlterField(
            model_name="content",
            name="featured_image",
            field=cloudinary.models.CloudinaryField(
                max_length=255, verbose_name="Featured Image"
            ),
        ),
    ]
