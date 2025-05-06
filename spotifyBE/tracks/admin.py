from django.contrib import admin
from spotifyBE.tracks.models import Tracks
from django.utils.html import format_html
from django.core.exceptions import ValidationError

@admin.register(Tracks)
class TracksAdmin(admin.ModelAdmin):
    # Hiển thị tất cả các trường trong danh sách
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields if field.name != 'lyrics']

    # Bật tính năng sửa và xóa cho các trường
    actions = ['delete_selected']  # Cho phép xóa nhiều bản ghi cùng lúc
    
    # Thêm search_fields để hỗ trợ autocomplete
    search_fields = ['title', 'status']
    
    # Thêm filter cho các trường
    list_filter = ['status', 'releaseDate']
    
    # Các trường hiển thị trên trang danh sách
    list_display = ('id', 'title', 'duration_formatted', 'release_date_formatted', 'playCount', 'status', 'preview_image')
    
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
            'fields': ('track_file', 'video_file')
        }),
        ('Hình ảnh', {
            'fields': ('image_file', 'preview_image_detail')
        }),
        ('Thông tin khác', {
            'fields': ('playCount', 'createdAt', 'lyrics')
        }),
    )
    
    # Tùy chỉnh hiển thị hình ảnh
    def preview_image(self, obj):
        if obj.image_file:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 5px;" />', obj.image_file.url)
        return "Không có hình ảnh"
    preview_image.short_description = 'Hình ảnh'
    
    def preview_image_detail(self, obj):
        if obj.image_file:
            return format_html('<img src="{}" width="150" height="150" style="object-fit: cover; border-radius: 8px;" />', obj.image_file.url)
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
            return ('title', 'duration', 'track_file', 'video_file', 'releaseDate', 'image_file', 'status', 'lyrics')
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

    # Add actions
    actions = ['make_published', 'make_draft']
    
    def make_published(self, request, queryset):
        queryset.update(status='published')
    make_published.short_description = "Đánh dấu các track đã chọn là đã xuất bản"
    
    def make_draft(self, request, queryset):
        queryset.update(status='draft')
    make_draft.short_description = "Đánh dấu các track đã chọn là bản nháp"

    # Add custom validation
    def clean(self):
        if self.duration <= 0:
            raise ValidationError("Thời lượng phải lớn hơn 0")