# music/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from spotifyBE.albums.views import AlbumsViewSet

router = DefaultRouter()
router.register('albums', AlbumsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]