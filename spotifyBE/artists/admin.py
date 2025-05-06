
from django.contrib import admin
from spotifyBE.artists.models import Artists

@admin.register(Artists)
class ArtistsAdmin(admin.ModelAdmin):
    # Hiển thị tất cả các trường trong danh sách
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]

    # Bật tính năng sửa và xóa cho các trường
    actions = ['delete_selected']  # Cho phép xóa nhiều bản ghi cùng lúc

    search_fields = ['name', 'gender']  # Cho phép tìm kiếm theo tên và thể loại

