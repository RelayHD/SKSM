from django.urls import path

# from sgkm_web.main.views import search
from . import views
from main import views as mainview
from django.urls.conf import include


urlpatterns= [
    path('info/<str:tag>/', views.single_page),
    path('', include('main.urls')),
]