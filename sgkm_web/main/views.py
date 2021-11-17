from django.shortcuts import render
from django.urls.resolvers import URLPattern
from .models import Post, PostImages

def index(request):
    posts= Post.objects.all().order_by('-created_at')
    # photos= PostImages.objects.all().order_by()
    return render(
        request,
        'main/index.html',
        {
            'posts':posts,
            # 'photos':photos
        }
    )

def single_post_page(request, pk):
    post= Post.objects.get(pk=pk)
    photos= PostImages.objects.filter(post=post)

    return render(
        request,
        'main/single_post_page.html',
        {
            'post': post,
            'photos': photos
        }
    )