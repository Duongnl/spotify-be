# music/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from spotifyBE.playlists.views import PlaylistsViewSet

router = DefaultRouter()
router.register('playlists', PlaylistsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]