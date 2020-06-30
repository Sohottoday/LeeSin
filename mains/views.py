from .models import *
from . import main_crawling, model_crud
import time

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


def insite(request):
    return render(request, 'mains/insite.html')

# DB 생성용
def issue(request):
    URL = 'https://api.github.com/search/issues?q=language:'
    params = ['JavaScript', 'Java', 'Python', 'C', 'C#', 'C++', 'Go', 'Ruby', 'TypeScript', 'PHP', 'Scala', 'Rust', 'Kotlin', 'Swift', 'Shell']
    langcount = []

    for param in params:
        response = requests.get(URL+param)
        issue = response.json().get('total_count')
        langcount.append(issue)
        time.sleep(7)

    print(langcount)
    
    issuecounting = CountIssue(
        javascript=langcount[0],
        java=langcount[1],
        python=langcount[2],
        c=langcount[3],
        csharp=langcount[4],
        cplus=langcount[5],
        go=langcount[6],
        ruby=langcount[7],
        typescript=langcount[8],
        php=langcount[9],
        scala=langcount[10],
        rust=langcount[11],
        kotlin=langcount[12],
        swift=langcount[13],
        shell=langcount[14]  
    )    

    issuecounting.save()
    return render(request, 'mains/insite.html')


def repository(request):
    URL = 'https://api.github.com/search/repositories?q=language:'
    params = ['JavaScript', 'Java', 'Python', 'C', 'C#', 'C++', 'Go', 'Ruby', 'TypeScript', 'PHP', 'Scala', 'Rust', 'Kotlin', 'Swift', 'Shell']
    langcount = []

    for param in params:
        response = requests.get(URL+param)
        issue = response.json().get('total_count')
        langcount.append(issue)
        time.sleep(7)

    print(langcount)
    
    repocounting = CountRepository(
        javascript=langcount[0],
        java=langcount[1],
        python=langcount[2],
        c=langcount[3],
        csharp=langcount[4],
        cplus=langcount[5],
        go=langcount[6],
        ruby=langcount[7],
        typescript=langcount[8],
        php=langcount[9],
        scala=langcount[10],
        rust=langcount[11],
        kotlin=langcount[12],
        swift=langcount[13],
        shell=langcount[14]  
    )    

    repocounting.save()
    return render(request, 'mains/insite.html')





# def issuepython(request):
#     URL = 'https://api.github.com/search/issues?q=language:'
        
#     response = requests.get(URL+'python')
#     issue = response.json().get('total_count')
    
#     javascript = CountIssue(python=issue)     # f'{language}'
#     javascript.save()
#     return render(request, 'mains/insite.html')



