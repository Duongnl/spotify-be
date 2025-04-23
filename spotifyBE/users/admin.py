from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

class UserCreationForm(forms.ModelForm):
    """Form for creating new users. Includes all required fields, plus a repeated password."""
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Xác nhận mật khẩu', widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ('username', 'email', 'name', 'birthDay', 'gender')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Mật khẩu không khớp")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """Form for updating users. Includes all fields on the user, but replaces the
    password field with admin's disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField(
        label="Mật khẩu",
        help_text="Mật khẩu đã được mã hóa. Bạn không thể xem mật khẩu của người dùng, "
                  "nhưng bạn có thể thay đổi mật khẩu bằng cách <a href=\"../password/\">nhấp vào đây</a>."
    )

    class Meta:
        model = Users
        fields = ('username', 'email', 'password', 'name', 'birthDay', 'gender', 
                 'imageUrl', 'status', 'is_active', 'is_staff', 'is_superuser')

class CustomUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    
    # Các trường hiển thị trong danh sách người dùng
    list_display = ('username', 'email', 'name', 'gender', 'is_active', 'is_staff', 'is_superuser', 'createdAt')
    list_filter = ('is_active', 'is_staff', 'gender', 'status')
    
    # Trường tìm kiếm
    search_fields = ('username', 'email', 'name')
    ordering = ('-createdAt',)
    
    # Phân nhóm các trường khi xem/chỉnh sửa chi tiết người dùng
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Thông tin cá nhân', {'fields': ('email', 'name', 'birthDay', 'gender', 'imageUrl')}),
        ('Quyền hạn', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Trạng thái', {'fields': ('status',)}),
    )
    
    # Phân nhóm các trường khi thêm người dùng mới
    add_fieldsets = (
        (None, {
'classes': ('wide',),
            'fields': ('username', 'email', 'name', 'birthDay', 'gender', 'password1', 'password2'),
        }),
    )

# Đăng ký model Users với giao diện admin tùy chỉnh
admin.site.register(Users, CustomUserAdmin)
