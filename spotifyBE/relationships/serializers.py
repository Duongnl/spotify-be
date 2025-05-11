from rest_framework import serializers
from spotifyBE.relationships.models import AlbumTracks, ArtistTracks, PlaylistTracks
from spotifyBE.tracks.serializers import TracksSerializer
from spotifyBE.utils.simple_serializer import ArtistsSimpleSerializer
from spotifyBE.tracks.models import Tracks
from spotifyBE.playlists.models import Playlists

class AlbumTracksSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumTracks
        fields = '__all__'

class ArtistTracksSerializer(serializers.ModelSerializer):
    # artist = ArtistsSerializer()
    artist = ArtistsSimpleSerializer()
    track = TracksSerializer(read_only=True)
    class Meta:
        model = ArtistTracks
        fields = '__all__'

class PlaylistTracksSerializer(serializers.ModelSerializer):
    playlist_id = serializers.UUIDField(write_only=True)
    track_id = serializers.UUIDField(write_only=True)
    
    playlist = serializers.PrimaryKeyRelatedField(read_only=True)
    track = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = PlaylistTracks
        fields = '__all__' 
        
    def validate(self, attrs):
        playlist_id = attrs.get("playlist_id")
        track_id = attrs.get("track_id")

        if PlaylistTracks.objects.filter(playlist_id=playlist_id, track_id=track_id).exists():
            raise serializers.ValidationError("Track đã tồn tại trong playlist này.")
        return attrs

        
    def validate_track_id(self, value):
        """
        Kiểm tra xem artist_id có tồn tại trong cơ sở dữ liệu không.
        """
        try:
            track = Tracks.objects.get(id=value)
        except Exception as e:
            raise serializers.ValidationError(str(e))
        return value
    
    def validate_playlist_id(self, value):
        """
        Kiểm tra xem artist_id có tồn tại trong cơ sở dữ liệu không.
        """
        try:
            playlist = Playlists.objects.get(id=value)
        except Exception as e:
            raise serializers.ValidationError(str(e))
        return value
    