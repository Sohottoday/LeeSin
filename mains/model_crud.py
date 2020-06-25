import re
from .models import *

def insert_stack(name):
    stack = Stack(name=name)
    stack.save()

def detail_null_stack():
    stack = Stack.objects.all()
    filered_stk = stack.filter(detail__isnull=True)
    for item in filered_stk:
        print(item.name)

def check_item_in_model(search_stack):
    # print(search_stack)
    try:
        finded_stack = Stack.objects.get(name__icontains=search_stack)
        # 있을 때
    except Stack.DoesNotExist:
        # 없을 때
        # print(search_stack)
        this_split = re.split(' ',search_stack)
        if len(this_split)>1 :
            for item in this_split:
                check_item_in_model(item)