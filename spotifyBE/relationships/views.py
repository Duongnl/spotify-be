from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from spotifyBE.relationships.models import AlbumTracks, ArtistTracks, PlaylistTracks
from spotifyBE.relationships.serializers import (
    AlbumTracksSerializer,
    ArtistTracksSerializer,
    PlaylistTracksTracksSerializer
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
    """
    API endpoint for managing playlist-track relationships
    """
    queryset = PlaylistTracks.objects.all()
    serializer_class = PlaylistTracksTracksSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Optionally filter by playlist_id or track_id
        """
        queryset = PlaylistTracks.objects.all()
        playlist_id = self.request.query_params.get('playlist_id', None)
        track_id = self.request.query_params.get('track_id', None)
        
        if playlist_id is not None:
            queryset = queryset.filter(playlist_id=playlist_id)
        if track_id is not None:
            queryset = queryset.filter(track_id=track_id)
            
        return queryset
