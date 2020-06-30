from .models import *
from . import main_crawling, model_crud

from django.shortcuts import render
from django.db.models import Count
import requests

# Create your views here.


def index(request):
    main_crawling.init_setting()
    return render(request, 'mains/index.html')


def menu(request):

    return render(request, 'mains/menu.html')


def rank(request):

    # for item in stk_cnt:
    #     print(item)
    return render(request, 'mains/rank.html')


def content(request):
    stk_rank = SkillStack.objects.values('name', 'stackshareLink', 'img').annotate(
        Count('wants_stacks')).order_by('-wants_stacks__count')[:20]
    # print(stk_rank[0].img)
    context = {
        'stk_rank': stk_rank,
    }
    return render(request, 'mains/content.html', context)


def content1(request):
    return render(request, 'mains/content1.html')


def insite(request):
    return render(request, 'mains/insite.html')

# DB 생성용


def issuejavascript(request):
    URL = 'https://api.github.com/search/issues?q=language:'
    params = ['javascript', 'java']

    for param in params:
        response = requests.get(URL+param)
        issue = response.json().get('total_count')

    javascript = CountIssue(javascript=issue)
    javascript.save()
    return render(request, 'mains/insite.html')
