from rest_framework import serializers
from spotifyBE.artists.models import Artists

class ArtistsNestedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Artists
        fields = '__all__'
        extra_kwargs = {
            'track_file': {'required': False},
            'video_file': {'required': False},
            'image_file': {'required': False},
        }