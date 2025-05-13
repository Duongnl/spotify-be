from rest_framework import status, generics
from rest_framework.views import APIView
from spotifyBE.users.models import Users
from .serializers import UsersSerializer, UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth.hashers import check_password
from spotifyBE.utils.custom_token import get_tokens_for_user
from spotifyBE.utils.response import ApiResponse
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

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
        from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
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
        
class UserDetailView(generics.RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return ApiResponse(data=serializer.data)

    def get_object(self):
        return self.request.user

class UserByIdView(generics.RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return ApiResponse(data=serializer.data)

class UpdateUserView(generics.UpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.get(id=self.kwargs['id'])
        self.check_object_permissions(self.request, obj)
        return obj

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        print(f"Request data: {request.data}")  # Debug dữ liệu nhận được
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return ApiResponse(data=serializer.data, statusCode=status.HTTP_200_OK)
        return ApiResponse(error=serializer.errors, statusCode=status.HTTP_400_BAD_REQUEST)
    
class UpdateUserPlaybarIdView(generics.GenericAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.get(id=self.kwargs['id'])
        self.check_object_permissions(self.request, obj)
        return obj

    def post(self, request, *args, **kwargs):
        user = self.get_object()

        # Lấy playbar_id từ request data
        playbar_id = request.data.get('playbar_id')

        if not playbar_id:
            return ApiResponse(error="playbar_id is required", statusCode=status.HTTP_400_BAD_REQUEST)

        # Cập nhật playbar_id
        user.playbar_id = playbar_id
        user.save()

        # Trả về dữ liệu người dùng đã cập nhật
        serializer = self.get_serializer(user)
        return ApiResponse(data=serializer.data, statusCode=status.HTTP_200_OK)
