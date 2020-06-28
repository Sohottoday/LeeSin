from .recruit_company import CompanyCrawling
import re
from .models import *



class modelData:
    def __init__(self):
        self.com = None
        super().__init__()

    def find_company(self, company):
        try:
            com = Company.objects.get(name=company.name)
            self.com = com
        except Company.DoesNotExist:
            # 이거 추가해야함
            com = Company(name = company.name, scale = None)

        except:
            pass

    def insert_stack(self, name):
        stack = SkillStack(name=name)
        stack.save()


    def detail_null_stack(self):
        stack = SkillStack.objects.all()
        filered_stk = stack.filter(detail__isnull=True)
        for item in filered_stk:
            print(item.name)


    def check_item_in_model(self, search_stack):
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
