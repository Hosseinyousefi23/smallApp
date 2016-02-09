from django import template

register = template.Library()


@register.filter
def to_persian(value):
    if value == 'username':
        return 'نام کاربری'

    elif value == 'password':
        return 'رمز عبور'

    elif value == 'confirm_password':
        return 'تایید رمز عبور'

    elif value == 'student_id':
        return 'شماره دانشجویی یا پرسنلی'

    elif value == 'university':
        return 'دانشگاه'
