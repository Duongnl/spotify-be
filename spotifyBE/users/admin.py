from django.contrib import admin
from .models import Users

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'name', 'imageUrl', 'status')  # Thêm imageUrl vào đây
    fields = ('username', 'email', 'name', 'imageUrl', 'birthDay', 'gender', 'status')  # Thêm imageUrl vào form chi tiết

admin.site.register(Users, UsersAdmin)