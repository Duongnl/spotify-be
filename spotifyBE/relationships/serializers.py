from rest_framework import serializers
from spotifyBE.relationships.models import AlbumTracks, ArtistTracks, PlaylistTracks

class AlbumTracksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AlbumTracks
        fields = '__all__'

class ArtistTracksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArtistTracks
        fields = '__all__'

class PlaylistTracksTracksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlaylistTracks
        fields = '__all__' 