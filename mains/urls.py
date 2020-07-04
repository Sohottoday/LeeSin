from django.urls import path
from . import views

app_name = 'mains'
urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('rank/', views.rank, name='rank'),
    path('content/', views.content, name='content'),
    path('content/json', views.contentjson, name='contentjson'),
    path('content/<str:lang>/', views.langfilter, name='langfilter'),
    path('insite/', views.insite, name='insite'),
    path('insitetest/', views.insitetest, name='insitetest'),
    path('insite/json', views.insitejson, name='insitejson'),
   
    # DB 생성용
    path('issue/', views.issue, name='issue'),
    path('repository/', views.repository, name='repository'),
    
    # 계산 하는것
    path('setting/', views.setting, name='setting'),
    


    
    # path('content1/', views.content1, name='content1'),
]
