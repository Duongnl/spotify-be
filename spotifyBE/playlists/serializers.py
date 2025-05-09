from rest_framework import serializers
from spotifyBE.playlists.models import Playlists
from spotifyBE.users.models import Users

from spotifyBE.users.nested_serializers import UsersNestedSerializer
from spotifyBE.relationships.nested_serializers import PlaylistTracksNestedSerializer

class PlaylistsSerializer(serializers.ModelSerializer):
    
    user =  UsersNestedSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    tracks = PlaylistTracksNestedSerializer(many=True, read_only=True)
    
    class Meta:
        model = Playlists
        fields = '__all__'

    def validate_user_id(self, value):
        """
        Kiểm tra xem track_id có tồn tại trong cơ sở dữ liệu không.
        """
        try:
            user = Users.objects.get(id=value)
        except Exception as e:
            raise serializers.ValidationError(str(e))
        return value
    