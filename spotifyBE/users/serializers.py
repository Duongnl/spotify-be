from rest_framework import serializers
from spotifyBE.users.models import Users
from django.contrib.auth.hashers import make_password
import datetime
from spotifyBE.utils.validators import NAME_VALIDATOR
from spotifyBE.playlists.nested_serializers import PlaylistsNestedSerializer
from spotifyBE.playbar.nested_serializers import PlaybarNestedSerializer


class UsersSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex_verbose', read_only=True)
    playlists =  PlaylistsNestedSerializer(many=True, read_only=True)
    playbar = PlaybarNestedSerializer(read_only=True)
    class Meta:
        model = Users
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        user = Users.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data.get('name', ''),
            birthDay=validated_data.get('birthDay'),
            gender=validated_data.get('gender'),
        )
        return user

class UserRegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)
    
    class Meta:
        model = Users
        fields = ['username', 'email', 'password', 'password_confirm', 'name', 'birthDay', 'gender']
        extra_kwargs = {
            'password': {'write_only': True},
            'name': {'validators': [NAME_VALIDATOR]}  # Áp dụng validator cho trường name
        }
    
    def validate(self, data):
        if data['password'] != data.pop('password_confirm'):
            raise serializers.ValidationError("Mật khẩu xác nhận không khớp.")
        return data
    
    def create(self, validated_data):
        user = Users(
            username=validated_data['username'],
            email=validated_data['email'],
            name=validated_data['name'],
            birthDay=validated_data['birthDay'],
            gender=validated_data['gender'],
            password=make_password(validated_data['password']),
            createdAt=datetime.datetime.now(),
            status='active'
        )
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
