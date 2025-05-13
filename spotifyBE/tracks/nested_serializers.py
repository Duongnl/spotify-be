from rest_framework import serializers
from spotifyBE.tracks.models import Tracks


class TracksNestedSerializer(serializers.ModelSerializer):
    artistName = serializers.SerializerMethodField()
    class Meta:
        model = Tracks
        fields = '__all__'
        
    def get_artistName(self, obj):
        return [artist_track.artist.name for artist_track in obj.artists.all()]
        
