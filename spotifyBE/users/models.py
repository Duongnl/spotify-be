import uuid
from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_column='id')
    username = models.CharField(max_length=255,db_column="username")
    email = models.CharField(max_length=255,db_column="email")
    password = models.CharField(max_length=255,db_column="password")
    name = models.CharField(max_length=255,db_column="name")
    imageUrl = models.CharField(max_length=255,db_column="image_url", null=True)
    birthDay = models.DateField(max_length=255,db_column="birth_day")
    gender = models.CharField(max_length=255,db_column="gender")
    createdAt = models.DateTimeField(db_column="created_at")
    status = models.CharField(max_length=255,db_column="status")
    
    class Meta:
        db_table = 'users'