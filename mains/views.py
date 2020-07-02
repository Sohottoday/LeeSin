from .models import *
from . import main_crawling, model_crud

from django.http import JsonResponse
from django.db.models import Subquery
from django.shortcuts import render
from django.db.models import F, Sum, Count, Case, When
from django.db.models import Q

import time
import requests

# Create your views here.


def index(request):
    # main_crawling.init_setting()

    return render(request, 'mains/index.html')


def menu(request):

    return render(request, 'mains/menu.html')


def rank(request):

    # for item in stk_cnt:
    #     print(item)
    return render(request, 'mains/rank.html')


def content(request):
    stk_rank = SkillStack.objects.values('name', 'stackshareLink', 'img').annotate(
        Count('posted_recruit')).order_by('-posted_recruit__count')[:20]
    # print(stk_rank[0].img)
    # print(stk_rank)
    context = {
        'stk_rank': stk_rank,
    }
    return render(request, 'mains/content.html', context)


def content1(request):
    return render(request, 'mains/content1.html')


def insite(request):
    return render(request, 'mains/insite.html')

# def langfilter(request, lang):
#     result = None
#     filtered = Recruit.objects.filter(id__in=Subquery(SkillStack.objects.get(name__iexact=lang).
#                 posted_recruit.values('id'))).values('wants_stacks').\
#                 annotate(Count("wants_stacks")).order_by('-wants_stacks__count')
#     print(filtered)
#     stk_rank = SkillStack.objects.filter(name__in = Subquery(
#         filtered.values('wants_stacks')[:10]
#     ))
#     # filtered = SkillStack.objects.extra(tables=filtered, where=['filtered.wants_stacks=skillstack.name'])
#     # filtered = SkillStack.objects.filter(name=filtered)
#     # print(filtered.query)
#     # filtered = SkillStack.objects.filter(
#     #             name__in = Subquery(Recruit.objects.filter(
#     #                 id__in=Subquery(SkillStack.objects.get(name__iexact=lang).
#     #                 posted_recruit.values('id')))
#     #                 .values('wants_stacks')\
#     #                 .annotate(Count("wants_stacks")).
#     #                 order_by('-wants_stacks__count').
#     #                 values('wants_stacks')))
#     # print(filtered)
    

#     # result = SkillStack.objects.extra(tables= [filtered], where = ['filtered.wants_stacks=skillstack.name'])
#     # stk = filtered.objects.select_related('SkillStack')

#     # print(filtered)
#         # print(SkillStack.objects.get(name = item.wants_stacks))
#     # stk_rank = None
#     # for idx, item in enumerate(filtered):
#     #     if idx == 0:
#     #         stk_rank = SkillStack.objects.filter(name=item.get('wants_stacks'))
#     #     else:
#     #         stk_rank = stk_rank.union(SkillStack.objects.filter(name=item.get('wants_stacks')))

#     # print(stk_rank)
#     context = {
#         'stk_rank' : stk_rank,
#     }

#     return render(request, 'mains/content.html', context)



# DB 생성용


def issue(request):
    URL = 'https://api.github.com/search/issues?q=language:'
    params = ['JavaScript', 'Java', 'Python', 'C', 'C#', 'C++', 'Go', 'Ruby',
              'TypeScript', 'PHP', 'Scala', 'Rust', 'Kotlin', 'Swift', 'Shell']
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
    params = ['JavaScript', 'Java', 'Python', 'C', 'C#', 'C++', 'Go', 'Ruby',
              'TypeScript', 'PHP', 'Scala', 'Rust', 'Kotlin', 'Swift', 'Shell']
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
