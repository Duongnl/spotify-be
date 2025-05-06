from rest_framework import serializers
from spotifyBE.albums.models import Albums

from spotifyBE.utils.validators import NAME_VALIDATOR

class AlbumsNestedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Albums
        fields = '__all__'