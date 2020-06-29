from .recruit_company import CompanyCrawling
from .recruit_detail import RecruitCrawling
from .recruit_stack import StackCrawling
from . import model_crud

import pprint
import re
import requests
from bs4 import BeautifulSoup

wordDic = {}

def crawling():
    site = 'programmers'
    for num in range(1845, 1845+1):
        url = f'https://programmers.co.kr/job_positions/{num}'
        responce = requests.get(url)

        soup = BeautifulSoup(responce.text, 'html.parser')
        print(num)

        is_recruit = soup.select(
            'body > div.main > div.position-show > div > div > \
                div.content-body.col-item.col-xs-12.col-sm-12.col-md-12.col-lg-8'
        )
        if not is_recruit:
            continue

        pp = pprint.PrettyPrinter()

        # 회사 정보 크롤링
        company = CompanyCrawling()
        company.crawling_compnay_all(soup)
        # pp.pprint(company.__dict__)
        pp.pprint(company.__dict__)
        
        # 공고 정보 크롤링
        recruit = RecruitCrawling(index=num, url=url, site = site)
        recruit.crawling_recruit_all(soup)
        # pp.pprint(recruit.__dict__)
        pp.pprint(recruit.__dict__)

        # 200까지함
        stk = StackCrawling(num)
        # pp.pprint(stk.crawling_stack_all(soup))
        stacks = stk.crawling_stack_all(soup)
        
        model_crud.data_into_db(company,recruit,stacks)