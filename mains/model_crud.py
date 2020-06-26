import re
from .models import *


def insert_stack(name):
    stack = SkillStack(name=name)
    stack.save()


def detail_null_stack():
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
                    stackdic = {**stackdic,**reDic}
    except SkillStack.MultipleObjectsReturned:
        pass
    return stackdic
