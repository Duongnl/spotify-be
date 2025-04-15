from django.db import models
import uuid
# Create your models here.
class Tracks(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_column='id')
    title = models.CharField(max_length=255,db_column="title")
    duration = models.IntegerField(db_column="duration")
    urlTrack = models.CharField(max_length=255,db_column="url_track")
    urlVideo = models.CharField(max_length=255,db_column="url_video", null=True)
    releaseDate = models.DateField(db_column="release_date", null=True)
    imageUrl = models.CharField(max_length=255, db_column= "image_url", null=True)
    lyrics = models.TextField(db_column="lyrics", null=True)
    playCount = models.IntegerField(db_column="play_count")
    createdAt = models.DateTimeField(db_column="created_at")
    status = models.CharField(max_length=255,db_column="status", null=True)
    
    
    class Meta:
        db_table = 'tracks'
    
