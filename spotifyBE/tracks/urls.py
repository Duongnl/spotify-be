from django.urls import path, include
from rest_framework.routers import DefaultRouter
from spotifyBE.tracks.views import TracksViewSet

router = DefaultRouter()
router.register('tracks', TracksViewSet)

urlpatterns = [
    path('', include(router.urls)),
]