from rest_framework import serializers
from spotifyBE.tracks.models import Tracks

class TracksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        modal = Tracks
        field = '__all__'