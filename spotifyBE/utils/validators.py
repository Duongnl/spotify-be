from django.core.exceptions import ValidationError
import regex  # pip install regex

def NAME_VALIDATOR(value):
    # Cho phép tất cả chữ cái Unicode (bao gồm tiếng Việt) và khoảng trắng
    pattern = r'^[\p{L}\s]+$'
    # Dùng fullmatch để kiểm tra toàn bộ chuỗi
    if not regex.fullmatch(pattern, value):
        raise ValidationError(
            'The title can only contain alphabetic characters (including Vietnamese) and spaces, and must not contain numbers or special characters.'
        )
