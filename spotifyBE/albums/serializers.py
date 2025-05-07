from rest_framework import serializers
from spotifyBE.albums.models import Albums
from spotifyBE.artists.models import Artists
# from spotifyBE.artists.serializers import ArtistsSerializer
from spotifyBE.utils.validators import NAME_VALIDATOR
from spotifyBE.artists.nested_serializers import ArtistsNestedSerializer
from spotifyBE.relationships.nested_serializers import AlbumTracksNestedSerializer

class AlbumsSerializer(serializers.ModelSerializer):
    # artist = ArtistsSerializer(read_only=True) 
    # artist_id = serializers.UUIDField(write_only=True)
    
    title = serializers.CharField(validators=[NAME_VALIDATOR])
    artist = ArtistsNestedSerializer(read_only=True)
    tracks = AlbumTracksNestedSerializer (many = True, read_only=True)
    class Meta:
        model = Albums
        fields = '__all__'
        
    def validate_artist_id(self, value):
        """
        Kiểm tra xem artist_id có tồn tại trong cơ sở dữ liệu không.
        """
        try:
            artist = Artists.objects.get(id=value)
        except Exception as e:
            raise serializers.ValidationError(str(e))
        return value



    