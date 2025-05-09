from django.db import models

# Create your models here.
from spotifyBE.tracks.models import Tracks
# Create your models here.
import uuid
# Create your models here.
class Playbar(models.Model):
    id = models.AutoField(primary_key=True)
    track = models.ForeignKey(Tracks, on_delete=models.CASCADE, db_column='track_id', related_name='playbars')
    currentTime =models.IntegerField(db_column="current_time", default=0)
    is_repeat = models.BooleanField(default=False)  # Trạng thái lặp lại bài hát

    
    class Meta:
        db_table = 'playbar'