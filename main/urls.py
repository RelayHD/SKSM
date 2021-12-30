from django.urls import path
from . import views

urlpatterns= [
    path('<int:pk>', views.single_post_page),
    path('', views.index),
    path('search/', views.search, name='search'),
    path('year/<int:year>',views.year, name='year'),
]