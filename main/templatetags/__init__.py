from django import template
import re
register = template.Library()

@register.filter
def add_link(value):
    content = value.content # 전달된 value 객체의 content 멤버변수를 가져온다.
    urls = re.findall(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))", value)    
    # tags의 각각의 인스턴를(tag)를 순회하며, content 내에서 해당 문자열을 => 링크를 포함한 문자열로 replace 한다.
    for url in urls:
        url_divide= url.split("|")
        content = re.sub(url,'<a href="'+url_divide[0]+'">'+url_divide[1]+'</a>', content)
    return content # 원하는 문자열로 치환이 완료된 content를 리턴한다.