from rest_framework import serializers
from spotifyBE.relationships.models import ArtistTracks, AlbumTracks, PlaylistTracks
from spotifyBE.artists.nested_serializers import ArtistsNestedSerializer
from spotifyBE.tracks.nested_serializers import TracksNestedSerializer


class ArtistTracksNestedRtArtistsSerializer(serializers.ModelSerializer):
    artist = ArtistsNestedSerializer(read_only=True)
    class Meta:
        model = ArtistTracks
        fields = '__all__'
        
class ArtistTracksNestedRtTracksSerializer(serializers.ModelSerializer):
    track = TracksNestedSerializer(read_only=True)
    class Meta:
        model = ArtistTracks
        fields = '__all__'

class AlbumTracksNestedSerializer(serializers.ModelSerializer):
    track = TracksNestedSerializer(read_only=True)
    class Meta:
        model = AlbumTracks
        fields = '__all__'
        
class PlaylistTracksNestedSerializer(serializers.ModelSerializer):
    track = TracksNestedSerializer(read_only=True)
    class Meta:
        model = PlaylistTracks
        fields = '__all__'
        