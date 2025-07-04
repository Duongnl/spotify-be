import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from cloudinary.models import CloudinaryField
from spotifyBE.playbar.models import Playbar

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email là bắt buộc')
        if not username:
            raise ValueError('Username là bắt buộc')
            
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            **extra_fields
        )
        user.set_password(password)  # Hash mật khẩu
        user.save(using=self._db)
        return user
        
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        return self.create_user(username, email, password, **extra_fields)

class Users(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, db_column="id")
    username = models.CharField(max_length=255, unique=True, db_column="username")
    email = models.EmailField(max_length=255, unique=True, db_column="email")
    # Xóa password = models.CharField(max_length=255, db_column="password")
    name = models.CharField(max_length=255, db_column="name")
    imageUrl = CloudinaryField('image', db_column="image_url", null=True, blank=True)
    birthDay = models.DateField(db_column="birth_day", null=True, blank=True)
    gender = models.CharField(max_length=255, db_column="gender", null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True, db_column="created_at")
    status = models.CharField(max_length=255, db_column="status", default='active')
    playbar = models.OneToOneField(Playbar, on_delete=models.CASCADE, db_column='playbar_id', related_name='user', null=True, default=None)
    
    # Các trường bắt buộc cho AbstractBaseUser
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    class Meta:
        db_table = 'users'

    def set_password(self, raw_password):
        super().set_password(raw_password)  # Sử dụng cơ chế hash của AbstractBaseUser