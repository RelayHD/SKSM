from django.shortcuts import render,get_object_or_404,redirect
from django.urls.resolvers import URLPattern
from django.core.paginator import Paginator
from .models import Post
from single_pages import models as singe_model

def index(request):
    posts= Post.objects.all().order_by('-created_at')
    indi_pages= singe_model.SinglePost.objects.all().order_by('tag')
    years=[]
    for post in posts:
        created_at= post.created_at
        year= created_at.year
        years.append(year)
    years= list(set(years))
    years.sort(reverse=True)
    paginator = Paginator(posts, 5)
    page= request.GET.get('page')
    post_a_page= paginator.get_page(page)
    return render(
        request,
        'main/postlist.html',
        {
            'years':years,
            'posts':post_a_page,
            'indi': indi_pages
        }
    )

def single_post_page(request, pk):
    posts= Post.objects.all().order_by('-created_at')
    indi_pages= singe_model.SinglePost.objects.all().order_by('tag')

    post= Post.objects.get(pk=pk)
    
    years=[]
    for p in posts:
        created_at= p.created_at
        year= created_at.year
        years.append(year)
    years= list(set(years))
    years.sort(reverse=True)
    return render(
        request,
        'main/single_post_page.html',
        {
            'years': years,
            'p': post,
            'indi': indi_pages

        }
    )

def search(request):
    posts= Post.objects.all().order_by('-created_at')
    indi_pages= singe_model.SinglePost.objects.all().order_by('tag')
    print("된다")
    years=[]
    for post in posts:
        created_at= post.created_at
        year= created_at.year
        years.append(year)
    years= list(set(years))
    years.sort(reverse=True)
    q= request.POST.get('q',"")
    
    print(q)
    if q:
        posts= posts.filter(title__icontains=q)
        paginator = Paginator(posts, 5)
        page= request.GET.get('page')
        post_a_page= paginator.get_page(page)
        return render(request, 'main/postlist.html', {'years':years,'posts':post_a_page, 'indi': indi_pages,"q":q})
    else:
        return render(request, 'main/postlist.html', {'years':years, 'indi': indi_pages,"q":q})


def year(request, year):
    posts= Post.objects.all().order_by('-created_at')
    indi_pages= singe_model.SinglePost.objects.all().order_by('tag')
    years=[]
    for post in posts:
        created_at= post.created_at
        ayear= created_at.year
        years.append(ayear)
    years= list(set(years))
    years.sort(reverse=True)

    year= year
    if year:
        posts= posts.filter(created_at__year=year)
        paginator = Paginator(posts, 5)
        page= request.GET.get('page')
        post_a_page= paginator.get_page(page)
        return render(request, 'main/postlist.html', {'years':years,'posts':post_a_page, 'indi': indi_pages})
    else:
        return render(request, 'main/postlist.html', {'years':years, 'indi': indi_pages})
