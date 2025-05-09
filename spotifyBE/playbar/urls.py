# music/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from spotifyBE.playbar.views import PlaybarViewSet

router = DefaultRouter()
router.register('playbar', PlaybarViewSet)

urlpatterns = [
    path('', include(router.urls)),
]