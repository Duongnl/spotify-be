from rest_framework import serializers
from spotifyBE.playlists.models import Playlists

class PlaylistsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Playlists
        fields = '__all__'

    