from django.shortcuts import render
from spotifyBE.albums.models import Albums
from rest_framework import viewsets
from spotifyBE.albums.serializers import AlbumsSerializer
from spotifyBE.artists.serializers import ArtistsSerializer
from spotifyBE.artists.models import Artists
from spotifyBE.utils.response import ApiResponse
from rest_framework.decorators import action
from http import HTTPStatus
# Create your views here.

class AlbumsViewSet(viewsets.ModelViewSet):
    queryset = Albums.objects.all()
    serializer_class = AlbumsSerializer

    def list(self, request, *args, **kwargs):
        albums = self.get_queryset()
        
        dataResponse = []
        for album in albums:
            album_serializer = self.get_serializer(album)
            artist_serializer = ArtistsSerializer(album.artist)
            
            album_data = album_serializer.data
            album_data["artist"] = artist_serializer.data
            
            dataResponse.append(album_data)
        
        return ApiResponse(data=dataResponse)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            album = self.get_object() # lay album ra
        except  Exception as e:
            return ApiResponse(error= str(e), statusCode=HTTPStatus.NOT_FOUND)
        
        album_serializer = self.get_serializer(album) # chuyen qua serializer khong can kiêm tra validator
        return ApiResponse(data=album_serializer.data)
    
    def create(self, request, *args, **kwargs):
        dataRequest = request.data # lay data request ra
        
        serializer = self.get_serializer(data=dataRequest) #bat dau chuyen qua kieu serializer va dong thoi kiem tra validator
        if not serializer.is_valid(): # neu loi thi tra ve loi
            return ApiResponse(error=serializer.errors, statusCode=HTTPStatus.BAD_REQUEST)
        
        # khong loi thi save serializer do
        serializer.save()
        return ApiResponse(data=serializer.data)
    
    def update(self, request, *args, **kwargs):
        try: 
            album = self.get_object() # lay album trong database ra
        except Exception as e:
            return ApiResponse(error=str(e), statusCode=HTTPStatus.NOT_FOUND)

        dataRequest = request.data
        
        partial = kwargs.get('partial', False) # dat trang thai cập nhật toàn bộ object
        serializer = self.get_serializer(album, data=dataRequest, partial=partial) # chuyenn qua serializer dong thoi tu kiem tra voi du lieu album cu va validator
        print("serializer >>> ", dataRequest)
        
        if not serializer.is_valid():
            return ApiResponse(error=serializer.errors, statusCode=HTTPStatus.BAD_REQUEST)
        
        serializer.save()
        return ApiResponse(data=serializer.data)
            
            
        
        
        
        

        
        
    