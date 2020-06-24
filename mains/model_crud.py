from .models import *


def insert_stack(name):
    stack = Stack(name=name)
    stack.save()

def detail_null_stack():
    stack = Stack.objects.all()
    filered_stk = stack.filter(detail__isnull=True)
    for item in filered_stk:
        print(item.name)
