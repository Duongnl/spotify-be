from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    
    # Thêm custom claims - đảm bảo chuyển UUID thành string
    refresh['user_id'] = str(user.id)
    refresh['username'] = user.username
    
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }