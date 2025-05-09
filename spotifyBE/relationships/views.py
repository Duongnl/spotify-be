from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from spotifyBE.relationships.models import AlbumTracks, ArtistTracks, PlaylistTracks
from spotifyBE.utils.response import ApiResponse
from rest_framework.decorators import action
from http import HTTPStatus
from spotifyBE.relationships.serializers import (
    AlbumTracksSerializer,
    ArtistTracksSerializer,
    PlaylistTracksSerializer
)

# Create your views here.

class AlbumTracksViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing album-track relationships
    """
    queryset = AlbumTracks.objects.all()
    serializer_class = AlbumTracksSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Optionally filter by album_id or track_id
        """
        queryset = AlbumTracks.objects.all()
        album_id = self.request.query_params.get('album_id', None)
        track_id = self.request.query_params.get('track_id', None)
        
        if album_id is not None:
            queryset = queryset.filter(album_id=album_id)
        if track_id is not None:
            queryset = queryset.filter(track_id=track_id)
            
        return queryset

class ArtistTracksViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing artist-track relationships
    """
    queryset = ArtistTracks.objects.all()
    serializer_class = ArtistTracksSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Optionally filter by artist_id or track_id
        """
        queryset = ArtistTracks.objects.all()
        artist_id = self.request.query_params.get('artist_id', None)
        track_id = self.request.query_params.get('track_id', None)
        
        if artist_id is not None:
            queryset = queryset.filter(artist_id=artist_id)
        if track_id is not None:
            queryset = queryset.filter(track_id=track_id)
            
        return queryset


class PlaylistTracksViewSet(viewsets.ModelViewSet):
    queryset = PlaylistTracks.objects.all()
    serializer_class = PlaylistTracksSerializer
    
    def create(self, request, *args, **kwargs):
        dataRequest = request.data # lay data request ra
        
        serializer = self.get_serializer(data=dataRequest) #bat dau chuyen qua kieu serializer va dong thoi kiem tra validator
        if not serializer.is_valid(): # neu loi thi tra ve loi
            return ApiResponse(error=serializer.errors, statusCode=HTTPStatus.BAD_REQUEST)
        
        # khong loi thi save serializer do
        serializer.save()
        return ApiResponse(data=serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except  Exception as e:
            return ApiResponse(error= str(e), statusCode=HTTPStatus.NOT_FOUND)

        self.perform_destroy(instance)
        return ApiResponse()
