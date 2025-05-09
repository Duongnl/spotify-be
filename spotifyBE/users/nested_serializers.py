from rest_framework import serializers
from spotifyBE.users.models import Users

class UsersNestedSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Users
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
        