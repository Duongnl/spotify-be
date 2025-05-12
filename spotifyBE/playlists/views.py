from django.shortcuts import render

# Create your views here.

from spotifyBE.playlists.models import Playlists
from rest_framework import viewsets
from spotifyBE.playlists.serializers import PlaylistsSerializer
from http import HTTPStatus
# Create your views here.
from spotifyBE.utils.response import ApiResponse
class PlaylistsViewSet(viewsets.ModelViewSet):
    queryset = Playlists.objects.all()
    serializer_class = PlaylistsSerializer
    
    def retrieve(self, request, *args, **kwargs):
        try:
            playlist = self.get_object() # lay album ra
        except  Exception as e:
            return ApiResponse(error= str(e), statusCode=HTTPStatus.NOT_FOUND)
        
        serializer = self.get_serializer(playlist) # chuyen qua serializer khong can kiêm tra validator
        return ApiResponse(data=serializer.data)
    
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
            playlist = self.get_object() # lay album trong database ra
        except Exception as e:
            return ApiResponse(error=str(e), statusCode=HTTPStatus.NOT_FOUND)

        dataRequest = request.data
        
        partial = kwargs.get('partial', False) # dat trang thai cập nhật toàn bộ object
        serializer = self.get_serializer(playlist, data=dataRequest, partial=partial) # chuyenn qua serializer dong thoi tu kiem tra voi du lieu album cu va validator
        
        print("serializer >>> ", dataRequest)
        
        if not serializer.is_valid():
            return ApiResponse(error=serializer.errors, statusCode=HTTPStatus.BAD_REQUEST)
        
        serializer.save()
        return ApiResponse(data=serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except  Exception as e:
            return ApiResponse(error= str(e), statusCode=HTTPStatus.NOT_FOUND)
        instance.tracks.all().delete()
        self.perform_destroy(instance)
        return ApiResponse()