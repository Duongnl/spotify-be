from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from spotifyBE.playlists.models import Playlists
from spotifyBE.playlists.serializers import PlaylistsSerializer

# API để lấy danh sách và tạo playlist
class PlaylistsListCreateAPIView(ListCreateAPIView):
    queryset = Playlists.objects.all()
    serializer_class = PlaylistsSerializer

# API để lấy, cập nhật, hoặc xóa một playlist cụ thể
class PlaylistsDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Playlists.objects.all()
    serializer_class = PlaylistsSerializer