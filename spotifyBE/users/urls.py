from django.urls import path
from .views import RegisterView, LoginView, RefreshTokenView, LogoutView, UserDetailView, UserByIdView, UpdateUserView, UpdateUserPlaybarIdView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/me/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:id>/', UserByIdView.as_view(), name='user-by-id'),
    path('users/update/<int:id>/', UpdateUserView.as_view(), name='update-user'),
    path('users/update-playbar/<int:id>/', UpdateUserPlaybarIdView.as_view(), name='update-user-playbar'),
]