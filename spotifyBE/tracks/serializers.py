from rest_framework import serializers
from spotifyBE.tracks.models import Tracks

class TracksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracks
        fields = '__all__'
        extra_kwargs = {
            'track_file': {'required': False},
            'video_file': {'required': False},
            'image_file': {'required': False},
        }