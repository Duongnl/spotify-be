# music/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from spotifyBE.artists.views import ArtistsViewSet

router = DefaultRouter()
router.register('artists', ArtistsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]