from rest_framework import serializers
from spotifyBE.playbar.models import Playbar
# from spotifyBE.relationships.serializers import ArtistTracksSerializer
from spotifyBE.tracks.nested_serializers import TracksNestedSerializer

class PlaybarNestedSerializer(serializers.ModelSerializer):
    track = TracksNestedSerializer(  read_only=True)
    class Meta:
        model = Playbar
        fields = '__all__'
       
