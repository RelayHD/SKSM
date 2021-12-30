from django import template
register = template.Library()

@register.filter
def check_empty(value):
    content = value # 전달된 value 객체의 content 멤버변수를 가져온다.
    if value.paragraph_1 == value.paragraph_2 == value.paragraph_3 == value.paragraph_4:
        return False
    else:
        return True
    