from rest_framework import serializers
from spotifyBE.users.models import Users

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        modal = Users
        field = '__all__'