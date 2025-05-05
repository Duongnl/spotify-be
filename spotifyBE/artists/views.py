from http import HTTPStatus
from django.shortcuts import render
from spotifyBE.artists.models import Artists
from rest_framework import viewsets
from spotifyBE.artists.serializers import ArtistsSerializer
from spotifyBE.albums.serializers import AlbumsSerializer
from spotifyBE.utils.response import ApiResponse
from spotifyBE.artists.serializers import ArtistsDetailSerializer
# Create your views here.

class ArtistsViewSet(viewsets.ModelViewSet):
    queryset = Artists.objects.all()
    serializer_class = ArtistsSerializer
    
    def list(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializer = self.get_serializer(data, many=True)
        return ApiResponse(data=serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            artist = self.get_object() # lay album ra
        except  Exception as e:
            return ApiResponse(error= str(e), statusCode=HTTPStatus.NOT_FOUND)
        
        # albums = artist.albums.all() #lay albums tu artist
        
        # artist_serializer = self.get_serializer(artist) # chuyen qua serializer khong can kiêm tra validator
        # album_serializer = AlbumsSerializer(albums, many=True) #many true la tai  vii nhiiieu truong du lieu
        
        # dataResponse = artist_serializer.data
        # dataResponse['albums'] = album_serializer.data
        artist_serializer = ArtistsDetailSerializer(artist) # chuyen qua serializer khong can kiêm tra validator
        
        return ApiResponse(data=artist_serializer.data)
    