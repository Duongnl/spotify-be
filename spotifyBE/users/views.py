from rest_framework import status, generics
from rest_framework.views import APIView
from spotifyBE.users.models import Users
from .serializers import UsersSerializer, UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth.hashers import check_password
from spotifyBE.utils.custom_token import get_tokens_for_user
from spotifyBE.utils.response import ApiResponse
from rest_framework.permissions import AllowAny

class RegisterView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            # Tạo token
            tokens = get_tokens_for_user(user)
            
            response_data = {
                'user': UsersSerializer(user).data,
                'tokens': {
                    'refresh': tokens['refresh'],
                    'access': tokens['access'],
                }
            }
            
            return ApiResponse(
                data=response_data,
                statusCode=status.HTTP_201_CREATED
            )
        return ApiResponse(
            error=serializer.errors,
            statusCode=status.HTTP_400_BAD_REQUEST
        )

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            try:
                user = Users.objects.get(username=username)
            except Users.DoesNotExist:
                return ApiResponse(
                    error="Username không tồn tại",
                    statusCode=status.HTTP_400_BAD_REQUEST
                )
            
            if check_password(password, user.password):
                # Tạo token
                tokens = get_tokens_for_user(user)
                
                response_data = {
                    'user': UsersSerializer(user).data,
                    'tokens': {
                        'refresh': tokens['refresh'],
                        'access': tokens['access'],
                    }
                }
                
                return ApiResponse(
                    data=response_data,
                    statusCode=status.HTTP_200_OK
                )
            else:
                return ApiResponse(
                    error="Mật khẩu không chính xác",
                    statusCode=status.HTTP_400_BAD_REQUEST
                )
        return ApiResponse(
            error=serializer.errors,
            statusCode=status.HTTP_400_BAD_REQUEST
        )

class RefreshTokenView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        from rest_framework_simplejwt.serializers import TokenRefreshSerializer
        serializer = TokenRefreshSerializer(data=request.data)
        
        if serializer.is_valid():
            return ApiResponse(
                data=serializer.validated_data,
                statusCode=status.HTTP_200_OK
            )
        return ApiResponse(
            error=serializer.errors,
            statusCode=status.HTTP_400_BAD_REQUEST
        )
class LogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        from rest_framework_simplejwt.tokens import OutstandingToken
        try:
            token = request.data.get('refresh')
            OutstandingToken.objects.filter(token=token).delete()
            return ApiResponse(
                data="Đăng xuất thành công",
                statusCode=status.HTTP_205_RESET_CONTENT
            )
        except Exception as e:
            return ApiResponse(
                error=str(e),
                statusCode=status.HTTP_400_BAD_REQUEST
            )