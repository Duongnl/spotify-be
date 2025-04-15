# Generated by Django 5.2 on 2025-04-15 19:38

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.UUIDField(db_column='id', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='username', max_length=255)),
                ('email', models.CharField(db_column='email', max_length=255)),
                ('password', models.CharField(db_column='password', max_length=255)),
                ('name', models.CharField(db_column='name', max_length=255)),
                ('imageUrl', models.CharField(db_column='image_url', max_length=255, null=True)),
                ('birthDay', models.DateField(db_column='birth_day', max_length=255)),
                ('gender', models.CharField(db_column='gender', max_length=255)),
                ('createdAt', models.DateTimeField(db_column='created_at')),
                ('status', models.CharField(db_column='status', max_length=255)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
