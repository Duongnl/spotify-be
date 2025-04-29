from django.contrib import admin
from spotifyBE.tracks.models import Tracks
from django.utils.html import format_html

@admin.register(Tracks)
class TracksAdmin(admin.ModelAdmin):
    # Các trường hiển thị trên trang danh sách
    list_display = ('id', 'title', 'duration_formatted', 'release_date_formatted', 'playCount', 'status', 'preview_image')
    
    # Trường cho phép tìm kiếm
    search_fields = ('title', 'lyrics')
    
    # Bộ lọc ở sidebar
    list_filter = ('status', 'releaseDate')
    
    # Sắp xếp mặc định
    ordering = ('-createdAt',)
    
    # Số lượng bản ghi trên mỗi trang
    list_per_page = 20
    
    # Các trường cho phép chỉnh sửa nhanh trên trang danh sách
    list_editable = ('status',)
    
    # Trường chỉ đọc khi chỉnh sửa
    readonly_fields = ('id', 'createdAt', 'playCount', 'preview_image_detail')
    
    # Phân nhóm các trường khi hiển thị form chỉnh sửa
    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('id', 'title', 'duration', 'releaseDate', 'status')
        }),
        ('Nội dung', {
            'fields': ('urlTrack', 'urlVideo', 'lyrics')
        }),
        ('Hình ảnh', {
            'fields': ('imageUrl', 'preview_image_detail')
        }),
        ('Thông tin khác', {
            'fields': ('playCount', 'createdAt')
        }),
    )
    
    # Tùy chỉnh hiển thị hình ảnh
    def preview_image(self, obj):
        if obj.imageUrl:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 5px;" />', obj.imageUrl)
        return "Không có hình ảnh"
    preview_image.short_description = 'Hình ảnh'
    
    def preview_image_detail(self, obj):
        if obj.imageUrl:
            return format_html('<img src="{}" width="150" height="150" style="object-fit: cover; border-radius: 8px;" />', obj.imageUrl)
        return "Không có hình ảnh"
    preview_image_detail.short_description = 'Xem trước hình ảnh'
    
    # Định dạng hiển thị thời lượng (phút:giây)
    def duration_formatted(self, obj):
        minutes = obj.duration // 60
        seconds = obj.duration % 60
        return f"{minutes}:{seconds:02d}"
    duration_formatted.short_description = 'Thời lượng'
    
    # Định dạng hiển thị ngày phát hành
    def release_date_formatted(self, obj):
        if obj.releaseDate:
            return obj.releaseDate.strftime("%d/%m/%Y")
        return "Chưa có"
    release_date_formatted.short_description = 'Ngày phát hành'
    
    # Tùy chỉnh form khi thêm mới
    def get_fields(self, request, obj=None):
        if obj is None:  # Khi thêm mới
            return ('title', 'duration', 'urlTrack', 'urlVideo', 'releaseDate', 'imageUrl', 'lyrics', 'status')
        return super().get_fields(request, obj)
    
    # Tùy chỉnh quyền hạn
    def has_delete_permission(self, request, obj=None):
        # Chỉ cho phép xóa nếu người dùng là superuser
        return request.user.is_superuser
    
    # Tùy chỉnh khi lưu
    def save_model(self, request, obj, form, change):
        if not change:  # Khi thêm mới
            import django.utils.timezone
            obj.createdAt = django.utils.timezone.now()
            obj.playCount = 0
        super().save_model(request, obj, form, change)