from django.urls import path
from . import views

app_name = 'mains'
urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('rank/', views.rank, name='rank'),
    path('content/', views.content, name='content'),
    path('content1/', views.content1, name='content1'),

    path('insite/', views.insite, name='insite'),
   
    # DB 생성용
    path('issue/', views.issue, name='issue'),
    path('repository/', views.repository, name='repository'),
    


    
    # path('content1/', views.content1, name='content1'),
]
