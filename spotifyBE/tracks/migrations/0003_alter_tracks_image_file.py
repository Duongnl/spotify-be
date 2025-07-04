# Generated by Django 5.2 on 2025-05-05 08:22

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0002_remove_tracks_imageurl_remove_tracks_urlvideo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracks',
            name='image_file',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
