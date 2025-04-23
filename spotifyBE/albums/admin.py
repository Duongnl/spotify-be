# from django.contrib import admin

# # Register your models here.
# from spotifyBE.albums.models import Albums

# @admin.register(Albums)
# class AlbumsAdmin(admin.ModelAdmin):
#     list_display = ('name', 'genre', 'debut_date')  # Hiện cột trong danh sách
#     search_fields = ('name', 'genre')               # Cho phép tìm kiếm
#     list_filter = ('genre',)                        # Lọc theo thể loại



from django.contrib import admin
from spotifyBE.albums.models import Albums

@admin.register(Albums)
class AlbumsAdmin(admin.ModelAdmin):
    # Hiển thị tất cả các trường trong danh sách
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]

    # Tìm kiếm theo tất cả các trường trong model
    def get_search_fields(self, request):
        return [field.name for field in self.model._meta.fields]

    # Lọc theo tất cả các trường trong model
    # def get_list_filter(self, request):
    #     return [field.name for field in self.model._meta.fields if isinstance(field, models.CharField)]

    # Bật tính năng sửa và xóa cho các trường
    actions = ['delete_selected']  # Cho phép xóa nhiều bản ghi cùng lúc