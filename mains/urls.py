from django.urls import path
from . import views

app_name = 'mains'
urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('rank/', views.rank, name='rank'),
    path('content/', views.content, name='content'),
]
