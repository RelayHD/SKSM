from django.shortcuts import render
from django.urls.resolvers import URLPattern
from .models import SinglePost
from main import models as main_model

def single_page(request,tag):
    post= SinglePost.objects.filter(tag=tag)
    posts= main_model.Post.objects.all().order_by('-created_at')
    indi_pages= SinglePost.objects.all().order_by('tag')

    years=[]
    for a in posts:
        created_at= a.created_at
        ayear= created_at.year
        years.append(ayear)
    years= list(set(years))
    years.sort(reverse=True)

    return render(
        request,
        'single_pages/template.html',
        {
            'singlePage':post,
            'years':years,
            'indi': indi_pages,
        }
    )

# def contact(request):
#     post= SinglePost.objects.filter(tag="contact")
#     posts= main_model.Post.objects.all().order_by('-created_at')

#     years=[]
#     for a in posts:
#         created_at= a.created_at
#         ayear= created_at.year
#         years.append(ayear)
#     years= list(set(years))
    
#     return render(
#         request,
#         'single_pages/template.html',
#         {
#             'p': post,
#             'years': years
#         }
#     )