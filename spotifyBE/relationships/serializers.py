from rest_framework import serializers
from spotifyBE.relationships.models import AlbumTracks, ArtistTracks, PlaylistTracks
from spotifyBE.tracks.serializers import TracksSerializer
from spotifyBE.utils.simple_serializer import ArtistsSimpleSerializer

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

class PlaylistTracksTracksSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistTracks
        fields = '__all__' 