from django.db import models

from spotifyBE.albums.models import Albums
from spotifyBE.artists.models import Artists
from spotifyBE.playlists.models import Playlists
from spotifyBE.tracks.models import Tracks

# Create your models here.

class PlaylistTracks(models.Model):
    id = models.AutoField(primary_key=True)
    playlist = models.ForeignKey(Playlists, on_delete=models.CASCADE, db_column='playlist_id', related_name='tracks')
    track = models.ForeignKey(Tracks, on_delete=models.CASCADE, db_column='track_id', related_name='playlists')
    trackNumber = models.IntegerField(db_column="track_number")
    addedAt = models.DateTimeField(db_column="added_at")
    class Meta:
        db_table = 'playlist_tracks'

class ArtistTracks (models.Model):
    id = models.AutoField(primary_key=True)
    track = models.ForeignKey(Tracks, on_delete=models.CASCADE, db_column='track_id', related_name='artists')
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE, db_column='artist_id', related_name='tracks')
    owner = models.BooleanField(db_column="owner")
    class Meta:
        db_table = 'artist_tracks'

class AlbumTracks (models.Model):
    id = models.AutoField(primary_key=True)
    track = models.ForeignKey(Tracks, on_delete=models.CASCADE, db_column='track_id', related_name='albums')
    album = models.ForeignKey(Albums, on_delete=models.CASCADE, db_column='album_id', related_name='tracks')
    trackNumber = models.IntegerField(db_column="track_number")
    class Meta:
        db_table = 'album_tracks'
    
    