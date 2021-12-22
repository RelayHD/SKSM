from django import template
from PIL import Image
register = template.Library()

@register.filter
def change_size(value):
    content = value # 전달된 value 객체의 content 멤버변수를 가져온다.
    return value/2
    