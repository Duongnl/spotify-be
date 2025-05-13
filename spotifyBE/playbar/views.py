from django.shortcuts import render

# Create your views here.

from spotifyBE.playbar.models import Playbar
from rest_framework import viewsets
from spotifyBE.playbar.serializers import PlaybarSerializer
from http import HTTPStatus
# Create your views here.
from spotifyBE.utils.response import ApiResponse
class PlaybarViewSet(viewsets.ModelViewSet):
    queryset = Playbar.objects.all()
    serializer_class = PlaybarSerializer
    
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
            playbar = self.get_object() # lay album trong database ra
        except Exception as e:
            return ApiResponse(error=str(e), statusCode=HTTPStatus.NOT_FOUND)

        dataRequest = request.data
        
       
        serializer = self.get_serializer(playbar, data=request.data, partial=True) # chuyenn qua serializer dong thoi tu kiem tra voi du lieu album cu va validator
        
        print("serializer >>> ", dataRequest)
        
        if not serializer.is_valid():
            return ApiResponse(error=serializer.errors, statusCode=HTTPStatus.BAD_REQUEST)
        
        serializer.save()
        return ApiResponse(data=serializer.data)
    