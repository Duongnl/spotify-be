from django.contrib import admin
from spotifyBE.relationships.models import AlbumTracks, ArtistTracks, PlaylistTracks
from django.utils.html import format_html

@admin.register(AlbumTracks)
class AlbumTracksAdmin(admin.ModelAdmin):
    # Các trường hiển thị trên trang danh sách
    list_display = ('id', 'album_title', 'track_title', 'preview_track')
    
    # Trường cho phép tìm kiếm
    search_fields = ('album__title', 'track__title')
    
    # Bộ lọc ở sidebar
    list_filter = ('album__title', 'track__title')
    
    # Sắp xếp mặc định
    ordering = ('album__title',)
    
    # Số lượng bản ghi trên mỗi trang
    list_per_page = 20
    
    # Trường chỉ đọc khi chỉnh sửa
    readonly_fields = ('id', 'preview_track_detail')
    
    # Phân nhóm các trường khi hiển thị form chỉnh sửa
    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('id', 'album', 'track')
        }),
        ('Xem trước', {
            'fields': ('preview_track_detail',)
        }),
    )
    
    def album_title(self, obj):
        return obj.album.title
    album_title.short_description = 'Album'
    
    def track_title(self, obj):
        return obj.track.title
    track_title.short_description = 'Track'
    
    def preview_track(self, obj):
        if obj.track.image_file:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 5px;" />', obj.track.image_file)
        return "Không có hình ảnh"
    preview_track.short_description = 'Hình ảnh track'
    
    def preview_track_detail(self, obj):
        if obj.track.image_file:
            return format_html('<img src="{}" width="150" height="150" style="object-fit: cover; border-radius: 8px;" />', obj.track.image_file)
        return "Không có hình ảnh"
    preview_track_detail.short_description = 'Xem trước hình ảnh track'

@admin.register(ArtistTracks)
class ArtistTracksAdmin(admin.ModelAdmin):
    # Các trường hiển thị trên trang danh sách
    list_display = ('id', 'artist_name', 'track_title', 'owner', 'preview_track')
    
    # Trường cho phép tìm kiếm
    search_fields = ('artist__name', 'track__title')
    
    # Bộ lọc ở sidebar
    list_filter = ('owner', 'artist__name', 'track__title')
    
    # Sắp xếp mặc định
    ordering = ('artist__name', 'track__title')
    
    # Số lượng bản ghi trên mỗi trang
    list_per_page = 20
    
    # Các trường cho phép chỉnh sửa nhanh trên trang danh sách
    list_editable = ('owner',)
    
    # Trường chỉ đọc khi chỉnh sửa
    readonly_fields = ('id', 'preview_track_detail')
    
    # Phân nhóm các trường khi hiển thị form chỉnh sửa
    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('id', 'artist', 'track', 'owner')
        }),
        ('Xem trước', {
            'fields': ('preview_track_detail',)
        }),
    )
    
    def artist_name(self, obj):
        return obj.artist.name
    artist_name.short_description = 'Nghệ sĩ'
    
    def track_title(self, obj):
        return obj.track.title
    track_title.short_description = 'Track'
    
    def preview_track(self, obj):
        if obj.track.image_file:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 5px;" />', obj.track.image_file)
        return "Không có hình ảnh"
    preview_track.short_description = 'Hình ảnh track'
    
    def preview_track_detail(self, obj):
        if obj.track.image_file:
            return format_html('<img src="{}" width="150" height="150" style="object-fit: cover; border-radius: 8px;" />', obj.track.image_file)
        return "Không có hình ảnh"
    preview_track_detail.short_description = 'Xem trước hình ảnh track'

@admin.register(PlaylistTracks)
class PlaylistTracksAdmin(admin.ModelAdmin):
    # Các trường hiển thị trên trang danh sách
    list_display = ('id', 'playlist_name', 'track_title', 'added_at_formatted', 'preview_track')
    
    # Trường cho phép tìm kiếm
    search_fields = ('playlist__name', 'track__title')
    
    # Bộ lọc ở sidebar
    list_filter = ('playlist__name', 'track__title', 'addedAt')
    
    # Sắp xếp mặc định
    ordering = ('playlist__name',)
    
    # Số lượng bản ghi trên mỗi trang
    list_per_page = 20
    
    # Trường chỉ đọc khi chỉnh sửa
    readonly_fields = ('id', 'addedAt', 'preview_track_detail')
    
    # Phân nhóm các trường khi hiển thị form chỉnh sửa
    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('id', 'playlist', 'track', 'addedAt')
        }),
        ('Xem trước', {
            'fields': ('preview_track_detail',)
        }),
    )
    
    def playlist_name(self, obj):
        return obj.playlist.name
    playlist_name.short_description = 'Playlist'
    
    def track_title(self, obj):
        return obj.track.title
    track_title.short_description = 'Track'
    
    def added_at_formatted(self, obj):
        return obj.addedAt.strftime("%d/%m/%Y %H:%M")
    added_at_formatted.short_description = 'Thời gian thêm'
    
    def preview_track(self, obj):
        if obj.track.image_file:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 5px;" />', obj.track.image_file)
        return "Không có hình ảnh"
    preview_track.short_description = 'Hình ảnh track'
    
    def preview_track_detail(self, obj):
        if obj.track.image_file:
            return format_html('<img src="{}" width="150" height="150" style="object-fit: cover; border-radius: 8px;" />', obj.track.image_file)
        return "Không có hình ảnh"
    preview_track_detail.short_description = 'Xem trước hình ảnh track' 