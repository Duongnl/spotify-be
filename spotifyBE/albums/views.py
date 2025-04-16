from django.shortcuts import render
from spotifyBE.albums.models import Albums
from rest_framework import viewsets
from spotifyBE.albums.serializers import AlbumsSerializer
# Create your views here.

class AlbumsViewSet(viewsets.ModelViewSet):
    queryset = Albums.objects.all()
    serializer_class = AlbumsSerializer
    filterset_fields = ['artist']