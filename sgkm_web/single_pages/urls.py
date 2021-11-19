from django.urls import path
from . import views
from main import views as mainview

urlpatterns= [
    path('profile/', views.profile),
    path('contact/', views.contact),
    path('', mainview.index)
]