from django.contrib import admin
from spotifyBE.playlists.models import Playlists

@admin.register(Playlists)
class PlaylistsAdmin(admin.ModelAdmin):
    # Hiển thị các trường trong danh sách
    list_display = ('id', 'name', 'createdAt', 'updatedAt', 'status', 'user')
    
    # Thêm các trường tìm kiếm
    search_fields = ('name', 'status', 'user__username')
    
    # Thêm bộ lọc
    list_filter = ('status', 'createdAt', 'updatedAt')
    
    # Các trường chỉ đọc
    readonly_fields = ('id', 'createdAt', 'updatedAt')
    
    # Phân nhóm các trường trong form chi tiết
    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('id', 'name', 'status', 'user')
        }),
        ('Thông tin thời gian', {
            'fields': ('createdAt', 'updatedAt')
        }),
    )