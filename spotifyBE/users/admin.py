from django.contrib import admin
from .models import Users

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'name', 'imageUrl', 'status', 'playbar')
    fields = ('username', 'email', 'name', 'imageUrl', 'birthDay', 'gender', 'status', 'playbar')

admin.site.register(Users, UsersAdmin)