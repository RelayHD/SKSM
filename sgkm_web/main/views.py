from django.shortcuts import render
from django.urls.resolvers import URLPattern
from .models import Post

def index(request):
    posts= Post.objects.all().order_by('-created_at')

    return render(
        request,
        'main/index.html',
        {
            'posts':posts,
        }
    )

def single_post_page(request, pk):
    post= Post.objects.get(pk=pk)

    return render(
        request,
        'main/single_post_page.html',
        {
            'post': post,
        }
    )