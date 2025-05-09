from rest_framework import serializers
from spotifyBE.playbar.models import Playbar
from spotifyBE.tracks.models import Tracks
# from spotifyBE.relationships.serializers import ArtistTracksSerializer
from spotifyBE.tracks.nested_serializers import TracksNestedSerializer

class PlaybarSerializer(serializers.ModelSerializer):
    track = TracksNestedSerializer(  read_only=True)
    track_id = serializers.UUIDField(write_only=True)
    class Meta:
        model = Playbar
        fields = '__all__'
       
    def validate_track_id(self, value):
        """
        Kiểm tra xem track_id có tồn tại trong cơ sở dữ liệu không.
        """
        try:
            track = Tracks.objects.get(id=value)
        except Exception as e:
            raise serializers.ValidationError(str(e))
        return value