from rest_framework import serializers
from spotifyBE.tracks.models import Tracks
# from spotifyBE.relationships.serializers import ArtistTracksSerializer
from spotifyBE.relationships.nested_serializers import ArtistTracksNestedRtArtistsSerializer

class TracksSerializer(serializers.ModelSerializer):
    artists = ArtistTracksNestedRtArtistsSerializer( many=True, read_only=True)
    class Meta:
        model = Tracks
        fields = '__all__'
        extra_kwargs = {
            'track_file': {'required': False},
            'video_file': {'required': False},
            'image_file': {'required': False},
        }
