from rest_framework import serializers
from spotifyBE.artists.models import Artists

class ArtistsSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artists
        fields = '__all__'