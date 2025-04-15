from django.db import models
from spotifyBE.artists.models import Artists
# Create your models here.
import uuid
# Create your models here.
class Albums(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_column='id')
    title = models.CharField(max_length=255,db_column="title")
    releaseDate = models.DateField(db_column="release_date", null=True)
    createdAt = models.DateTimeField(db_column="created_at")
    imageUrl = models.CharField(max_length=255, db_column= "image_url",  null=True)
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE, db_column='artist_id', related_name='albums')
    
    class Meta:
        db_table = 'albums'