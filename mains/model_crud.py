from .models import *
from .recruit_company import CompanyCrawling
from .recruit_detail import RecruitCrawling
from .stack_crawl import Crawling_Stack
import re
from django.db.models import Max
import time

# 크롤링할 다음 인덱스를 반환
def get_start_number(site_name):
    result = Recruit.objects.filter(site=site_name).aggregate(Max('index'))
    # print(result)
    result = result.get('index__max')
    if result is None:
        return 0
    else:
        return result

# 
def data_into_db(company, recuit, stacks):
    com = find_company(company)
    posting = create_recruit(recuit)
    recruit_link_company(company=com, recuit=posting)
    stack_link_recruit(recuit=posting, stacks=stacks)


def find_company(company):
    try:
        com = Company.objects.get(name=company.name)
    except Company.DoesNotExist:
        # 이거 추가해야함
        com = Company(name=company.name, scale=company.scale,
                      homepage=company.homepage)
        com.save()
    except:
        com = Company.objects.filter(name=company.name)[0]
    return com


def create_recruit(recuit):
    posting = Recruit(title=recuit.title, carear=recuit.job, carear_start=recuit.carear_start,
                      carear_end=recuit.carear_end, recruit_page=recuit.url,
                      index=recuit.index, site=recuit.site)
    posting.save()
    return posting


def recruit_link_company(company, recuit):
    company.posted_recruit.add(recuit)

# DB에 기술 스택이 있는지 확인 및 삭제
def find_stack(name):
    try:
        stk = SkillStack.objects.get(name=name)
    except SkillStack.DoesNotExist:
        stk = SkillStack(name=name)
        stk.save()
    return stk


def stack_link_recruit(recuit, stacks):
    for name in stacks:
        stk = find_stack(name)
        recuit.wants_stacks.add(stk)


def detail_null_stack():
    filered_stk = SkillStack.objects.filter(category__isnull=True)
    for i in range(len(filered_stk)):
        cs = Crawling_Stack(filered_stk[i].name)
        result = cs.crawling_all()
        # if result:
        #     print(f'StackDB-error-occured-name : {filered_stk[i].name}')
        #     filered_stk[i].category = 'Error-occured'
        #     filered_stk[i].category = cs.stackshareLink
        #     filered_stk[i].save()
        #     continue
        try:
            filered_stk[i].img = cs.img
            filered_stk[i].detail = cs.detail
            filered_stk[i].stackshareLink = cs.stackshareLink
            filered_stk[i].webpage = cs.webpage
            filered_stk[i].category = cs.category
            # filered_stk[i].save()
        except Exception as e:
            print(f'StackDB-error-occured-name : {filered_stk[i].name}')
        filered_stk[i].save()
        time.sleep(1)


def check_item_in_model(search_stack):
    stackdic = {}
    try:
        finded_stack = SkillStack.objects.get(name__icontains=search_stack)
        stackdic[finded_stack.name] = True
    except SkillStack.DoesNotExist:
        this_split = re.split(' ', search_stack)
        if len(this_split) > 1:
            for item in this_split:
                reDic = check_item_in_model(item)
                if reDic:
                    stackdic = {**stackdic, **reDic}
    except SkillStack.MultipleObjectsReturned:
        pass
    return stackdic
