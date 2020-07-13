import time
import requests
import os
import pprint
import math
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter

from django.http import JsonResponse
from django.db.models import Count, Subquery
from django.shortcuts import render
from django.conf import settings

from .models import *
from . import main_crawling, model_crud

# Create your views here.


def index(request):
    # main_crawling.init_setting()
    return render(request, 'mains/index.html')


def menu(request):
    return render(request, 'mains/menu.html')


def rank(request):
    stk_rank = SkillStack.objects.filter(category='Language')\
        .annotate(Count('posted_recruit')).order_by('-posted_recruit__count')[:10]
    # for item in stk_rank:
    #     print(item)
    context = {
        'stk_rank': stk_rank,
    }
    return render(request, 'mains/rank.html', context)


def content(request):
    stk_rank = SkillStack.objects.exclude(category='Error-occured')\
        .values('name', 'stackshareLink', 'img')\
        .annotate(Count('posted_recruit')).order_by('-posted_recruit__count')[:15]

    context = {
        'stk_rank': stk_rank,
    }
    return render(request, 'mains/content.html', context)


def contentjson(request):
    stk_rank = list(SkillStack.objects.values('name', 'stackshareLink', 'img').annotate(
        Count('posted_recruit')).order_by('-posted_recruit__count'))[:70]
    # print(stk_rank)
    # for i in range(len(stk_rank)):
    #     print(stk_rank[i])
    return JsonResponse(stk_rank, safe=False)


def recruits(request, stk):
    recruits = list(Recruit.objects.filter(wants_stacks = stk).prefetch_related('posting_company').order_by('-created_at'))[:15]
    # print(recruits[0]._prefetched_objects_cache['posting_company'][0].name)
    context = {
        'recruits' : recruits,
    }
    return render(request, 'mains/recuits.html', context)


def insite(request):
    return render(request, 'mains/insite.html')


def insiterepo(request):
    return render(request, 'mains/insite2.html')


def insitejson(request):
    repos = list(
        CountRepository.objects.values(
            'date', 'javascript', 'java', 'python', 'c', 'csharp',
            'cplus', 'ruby', 'typescript', 'php',
        )
    )

    langname = {
        'javascript': 'JavaScript',
        'java': 'Java',
        'python': 'Python',
        'c': 'C',
        'csharp': 'C#',
        'cplus': 'C++',
        'ruby': 'Ruby',
        'typescript': 'Typescript',
        'php': 'PHP',
    }

    repolist = []
    for item in repos[0]:
        if item != 'date':
            dic = {
                'lang': langname.get(item),
            }
            datelist = []
            for reponum in range(len(repos)):
                datelist.append([repos[reponum].get('date'),
                                 int(repos[reponum].get(item))])
                # datelist.append([element.get('date'),math.log( int(element.get(item)), 1.5 )])

            dic['date'] = datelist
            repolist.append(dic)

    return JsonResponse(repolist, safe=False)


def langfilter(request, lang):
    stk = SkillStack.objects.get(name=lang)

    filtered = Recruit.objects.filter(id__in=Subquery(SkillStack.objects
                                                      .exclude(category='Error-occured').exclude(category='Languages').get(name__iexact=lang).
                                                      posted_recruit.values('id'))).values('wants_stacks').\
        annotate(Count("wants_stacks")).order_by('-wants_stacks__count')[:14]
    stk_rank = SkillStack.objects.exclude(category='Error-occured').exclude(category='Language').filter(name__in=Subquery(
        filtered.values('wants_stacks')
    ))[:6]
    context = {
        'stk': stk,
        'stk_rank': stk_rank,
    }

    return render(request, 'mains/filterd.html', context)

# DB 생성용


def recruitcrawling(request):
    main_crawling.init_setting()
    return render(request, 'mains/index.html')


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

    # print(langcount)

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
    #print(langcount)

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


def setting(request):
    issues = CountIssue.objects.all()

    javascript = []
    java = []
    python = []
    c = []
    csharp = []
    cplus = []
    go = []
    ruby = []
    typescript = []
    php = []
    scala = []
    rust = []
    kotlin = []
    swift = []
    shell = []
    date = []

    for issue in issues:
        javascript.append(int(issue.javascript))
        java.append(int(issue.java))
        python.append(int(issue.python))
        c.append(int(issue.c))
        csharp.append(int(issue.csharp))
        cplus.append(int(issue.cplus))
        go.append(int(issue.go))
        ruby.append(int(issue.ruby))
        typescript.append(int(issue.typescript))
        php.append(int(issue.php))
        scala.append(int(issue.scala))
        rust.append(int(issue.rust))
        kotlin.append(int(issue.kotlin))
        swift.append(int(issue.swift))
        shell.append(int(issue.shell))
        date.append(issue.date)
    # print(javascript)
    # print(java)

    # language = ['javascript', 'java', 'python', 'c', 'csharp', 'cplus', 'go', 'ruby',
    #  'typescript', 'php', 'scala', 'rust', 'kotlin', 'swift', 'shell', 'date']
    # langcount = [javascript, java, python, c, csharp, splus, go, ruby, typescript, php
    # scala, rust, kotlin, swift, shell, date]

    plt.cla()
    plt.plot(date, javascript, 'rs--')
    plt.xticks(date)
    plt.xlabel('Date')
    plt.ylabel('Issue')
    plt.title('Javascript')
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    plt.savefig(os.path.join(settings.BASE_DIR, 'mains', 'static',
                             'mains', 'images', 'javascriptgraph.png'))

    plt.cla()
    plt.plot(date, java, 'mo--')
    plt.xticks(date)
    plt.xlabel('Date')
    plt.ylabel('Issue')
    plt.title('Java')
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    plt.savefig(os.path.join(settings.BASE_DIR, 'mains',
                             'static', 'mains', 'images', 'javagraph.png'))

    plt.cla()
    plt.plot(date, python, 'c.-')
    plt.xticks(date)
    plt.xlabel('Date')
    plt.ylabel('Issue')
    plt.title('Python')
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    plt.savefig(os.path.join(settings.BASE_DIR, 'mains',
                             'static', 'mains', 'images', 'pythongraph.png'))

    plt.cla()
    plt.plot(date, c, 'rs-')
    plt.xticks(date)
    plt.xlabel('Date')
    plt.ylabel('Issue')
    plt.title('C')
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    plt.savefig(os.path.join(settings.BASE_DIR, 'mains',
                             'static', 'mains', 'images', 'cgraph.png'))

    plt.cla()
    plt.plot(date, csharp, 'm.-')
    plt.xticks(date)
    plt.xlabel('Date')
    plt.ylabel('Issue')
    plt.title('C#')
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    plt.savefig(os.path.join(settings.BASE_DIR, 'mains',
                             'static', 'mains', 'images', 'csharpgraph.png'))

    plt.cla()
    plt.plot(date, cplus, 'co--')
    plt.xticks(date)
    plt.xlabel('Date')
    plt.ylabel('Issue')
    plt.title('C++')
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    plt.savefig(os.path.join(settings.BASE_DIR, 'mains',
                             'static', 'mains', 'images', 'cplusgraph.png'))

    plt.cla()
    plt.plot(date, go, 'ro-')
    plt.xticks(date)
    plt.xlabel('Date')
    plt.ylabel('Issue')
    plt.title('GO')
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    plt.savefig(os.path.join(settings.BASE_DIR, 'mains',
                             'static', 'mains', 'images', 'gograph.png'))

    plt.cla()
    plt.plot(date, ruby, 'g^-.')
    plt.xticks(date)
    plt.xlabel('Date')
    plt.ylabel('Issue')
    plt.title('Ruby')
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    plt.savefig(os.path.join(settings.BASE_DIR, 'mains',
                             'static', 'mains', 'images', 'rubygraph.png'))

    plt.cla()
    plt.plot(date, typescript, 'yv--')
    plt.xticks(date)
    plt.xlabel('Date')
    plt.ylabel('Issue')
    plt.title('TypeScript')
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    plt.savefig(os.path.join(settings.BASE_DIR, 'mains', 'static',
                             'mains', 'images', 'typescriptgraph.png'))

    plt.cla()
    plt.plot(date, php, 'mD:')
    plt.xticks(date)
    plt.xlabel('Date')
    plt.ylabel('Issue')
    plt.title('PHP')
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    plt.savefig(os.path.join(settings.BASE_DIR, 'mains',
                             'static', 'mains', 'images', 'phpgraph.png'))

    plt.cla()
    plt.plot(date, scala, 'b*-')
    plt.xticks(date)
    plt.xlabel('Date')
    plt.ylabel('Issue')
    plt.title('Scala')
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    plt.savefig(os.path.join(settings.BASE_DIR, 'mains',
                             'static', 'mains', 'images', 'scalagraph.png'))

    plt.cla()
    plt.plot(date, rust, 'r>-')
    plt.xticks(date)
    plt.xlabel('Date')
    plt.ylabel('Issue')
    plt.title('Rust')
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    plt.savefig(os.path.join(settings.BASE_DIR, 'mains',
                             'static', 'mains', 'images', 'rustgraph.png'))

    plt.cla()
    plt.plot(date, kotlin, 'kx--')
    plt.xticks(date)
    plt.xlabel('Date')
    plt.ylabel('Issue')
    plt.title('Kotlin')
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    plt.savefig(os.path.join(settings.BASE_DIR, 'mains',
                             'static', 'mains', 'images', 'kotlingraph.png'))

    plt.cla()
    plt.plot(date, swift, 'c_:')
    plt.xticks(date)
    plt.xlabel('Date')
    plt.ylabel('Issue')
    plt.title('Swift')
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    plt.savefig(os.path.join(settings.BASE_DIR, 'mains',
                             'static', 'mains', 'images', 'swiftgraph.png'))

    plt.cla()
    plt.plot(date, shell, 'gh--')
    plt.xticks(date)
    plt.xlabel('Date')
    plt.ylabel('Issue')
    plt.title('Shell')
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    plt.savefig(os.path.join(settings.BASE_DIR, 'mains',
                             'static', 'mains', 'images', 'shellgraph.png'))
    return render(request, 'mains/insite.html')
