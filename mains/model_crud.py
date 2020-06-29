from .recruit_company import CompanyCrawling
from .recruit_detail import RecruitCrawling
import re
from .models import *


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


def insert_stack(name):
    stack = SkillStack(name=name)
    stack.save()
    return stack


def find_stack(name):
    try:
        stk = SkillStack.objects.get(name=name)
    except SkillStack.DoesNotExist:
        stk = insert_stack(name)
    return stk


def stack_link_recruit(recuit, stacks):
    for name in stacks:
        stk = find_stack(name)
        recuit.wants_stacks.add(stk)


def detail_null_stack(self):
    stack = SkillStack.objects.all()
    filered_stk = stack.filter(detail__isnull=True)
    for item in filered_stk:
        print(item.name)


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
