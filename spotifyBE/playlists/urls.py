from django.urls import path
from spotifyBE.playlists.views import PlaylistsDetailAPIView

urlpatterns = [
    path('playlists/<uuid:pk>/', PlaylistsDetailAPIView.as_view(), name='playlists-detail'),
]