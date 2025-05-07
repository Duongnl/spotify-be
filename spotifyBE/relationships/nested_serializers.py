from rest_framework import serializers
from spotifyBE.relationships.models import ArtistTracks, AlbumTracks
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