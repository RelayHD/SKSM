from django import template
import re
register = template.Library()

@register.filter
def add_link(value):
    content = value # 전달된 value 객체의 content 멤버변수를 가져온다.
    regex = 'http[s]?://(?:[a-zA-Z가-힣]|[0-9]|[$\-@\.&+:/?=]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls = re.findall(regex, content)    
    # tags의 각각의 인스턴를(tag)를 순회하며, content 내에서 해당 문자열을 => 링크를 포함한 문자열로 replace 한다.
    for url in urls:
        url_str= str(url)
        url_divide= url_str.split("@link")
        content = re.sub(url,'<br>'+'<a href='+''+url_divide[0]+'>'+url_divide[-1]+'</a>', content)

    return content # 원하는 문자열로 치환이 완료된 content를 리턴한다.