import uuid
from django.db import models

from spotifyBE.users.models import Users

# Create your models here.
class Playlists(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_column='id')
    name = models.CharField(max_length=255,db_column="name")
    createdAt = models.DateField(db_column="created_at", auto_now_add=True)
    status = models.CharField(max_length=255,db_column="status")
    users = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='user_id', related_name='playlists')

    class Meta:
        db_table = 'playlists'
