from rest_framework import serializers
from spotifyBE.albums.models import Albums
from spotifyBE.artists.serializers import ArtistsSerializer

class AlbumsSerializer(serializers.ModelSerializer):
    artist = ArtistsSerializer(read_only=True) 
    class Meta:
        model = Albums
        fields = '__all__'


    