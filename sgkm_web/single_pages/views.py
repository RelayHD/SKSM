from django.shortcuts import render
from django.urls.resolvers import URLPattern
from .models import SinglePost

def profile(request):
    post= SinglePost.objects.filter(tag="profile")

    return render(
        request,
        'single_pages/template.html',
        {
            'post': post,
        }
    )

def contact(request):
    post= SinglePost.objects.filter(tag="contact")

    return render(
        request,
        'single_pages/template.html',
        {
            'post': post,
        }
    )