from django.db import models
import uuid
import os

def track_upload_path(instance, filename):
    # Tạo đường dẫn lưu trữ file track dựa trên ID của track
    return f'tracks/{instance.id}/{filename}'

def video_upload_path(instance, filename):
    # Tạo đường dẫn lưu trữ file video dựa trên ID của track
    return f'tracks/{instance.id}/videos/{filename}'

def image_upload_path(instance, filename):
    # Tạo đường dẫn lưu trữ ảnh dựa trên ID của track
    return f'tracks/{instance.id}/images/{filename}'

class Tracks(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_column='id')
    title = models.CharField(max_length=255, db_column="title")
    duration = models.IntegerField(db_column="duration")
    track_file = models.FileField(upload_to=track_upload_path, db_column="url_track", null=True)
    video_file = models.FileField(upload_to=video_upload_path, db_column="url_video", null=True)
    image_file = models.ImageField(upload_to=image_upload_path, db_column="image_url", null=True)
    releaseDate = models.DateField(db_column="release_date", null=True)
    lyrics = models.TextField(db_column="lyrics", null=True)
    playCount = models.IntegerField(db_column="play_count", default=0)
    createdAt = models.DateTimeField(db_column="created_at", auto_now_add=True)
    status = models.CharField(max_length=255, db_column="status", null=True)

    class Meta:
        db_table = 'tracks'

    def __str__(self):
        return f"{self.id} - {self.title}"