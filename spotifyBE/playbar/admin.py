from django.contrib import admin

# Register your models here.

from spotifyBE.playbar.models import Playbar

@admin.register(Playbar)
class PlaybarAdmin(admin.ModelAdmin):
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