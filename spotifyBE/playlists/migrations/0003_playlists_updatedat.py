# Generated by Django 5.2 on 2025-05-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlists',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True, db_column='updated_at'),
        ),
    ]
