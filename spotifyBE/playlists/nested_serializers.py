from rest_framework import serializers
from spotifyBE.playlists.models import Playlists

class PlaylistsNestedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Playlists
        fields = '__all__'

    