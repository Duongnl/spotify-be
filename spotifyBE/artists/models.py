import uuid
from django.db import models

# Create your models here.
class Artists(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_column='id')
    name = models.CharField(max_length=255,db_column="name")
    bio = models.TextField(db_column="bio", null=True)
    title = models.CharField(max_length=255,db_column="title")
    imageUrl = models.CharField(max_length=255,db_column="image_url", null=True)
    gender = models.CharField(max_length=255,db_column="gender")
    
    class Meta:
        db_table = 'artists'

    def __str__(self):
        return f"{self.id} - {self.name}"
