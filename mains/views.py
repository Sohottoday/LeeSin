from .models import *
from . import main_crawling, model_crud

from django.shortcuts import render
from django.db.models import Count

# Create your views here.
def index(request):
    main_crawling.init_setting()
    return render(request, 'mains/index.html')


def menu(request):

    return render(request, 'mains/menu.html')


def rank(request):
    stk_cnt = SkillStack.objects.values('name').annotate(Count('wants_stacks')).order_by('-wants_stacks__count')
    stk = SkillStack.objects.all()
    
    context = {
        'stk' : stk,
        'stk_cnt' : stk_cnt,
    }
    
    # for item in stk_cnt:
    #     print(item)
    return render(request, 'mains/rank.html', context)


def content(request):
    return render(request, 'mains/content.html')


def content1(request):
    return render(request, 'mains/content1.html')