from rest_framework import serializers
from spotifyBE.tracks.models import Tracks


class TracksNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracks
        fields = '__all__'
        
