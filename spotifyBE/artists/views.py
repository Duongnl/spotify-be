from django.shortcuts import render
from spotifyBE.artists.models import Artists
from rest_framework import viewsets
from spotifyBE.artists.serializers import ArtistsSerializer

# Create your views here.

class ArtistsViewSet(viewsets.ModelViewSet):
    queryset = Artists.objects.all()
    serializer_class = ArtistsSerializer
    