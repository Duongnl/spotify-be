from django.urls import path, include
from rest_framework.routers import DefaultRouter
from spotifyBE.relationships.views import (
    AlbumTracksViewSet,
    ArtistTracksViewSet,
    PlaylistTracksViewSet
)

router = DefaultRouter()
router.register(r'album-tracks', AlbumTracksViewSet, basename='album-tracks')
router.register(r'artist-tracks', ArtistTracksViewSet, basename='artist-tracks')
router.register(r'playlist-tracks', PlaylistTracksViewSet, basename='playlist-tracks')

urlpatterns = [
    path('', include(router.urls)),
]
