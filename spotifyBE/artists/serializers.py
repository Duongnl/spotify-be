from rest_framework import serializers
from spotifyBE.artists.models import Artists
from spotifyBE.albums.models import Albums
from spotifyBE.relationships.serializers import ArtistTracksSerializer
from spotifyBE.albums.serializers import AlbumsSerializer

class ArtistsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Artists
        fields = '__all__'


class ArtistsDetailSerializer(serializers.ModelSerializer):
    tracks = ArtistTracksSerializer( many=True, read_only=True)
    albums = AlbumsSerializer(many=True, read_only=True)
    class Meta:
        model = Artists
        fields = '__all__'




    