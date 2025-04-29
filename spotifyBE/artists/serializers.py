from rest_framework import serializers
from spotifyBE.artists.models import Artists
from spotifyBE.albums.models import Albums

class ArtistsSerializer(serializers.ModelSerializer):
    # albums = SimpleAlbumsSerializer(many=True, read_only=True)
    class Meta:
        model = Artists
        fields = '__all__'

    