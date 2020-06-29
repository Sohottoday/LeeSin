from . import model_crud
from .recruit_stack import StackCrawling
from .recruit_detail import RecruitCrawling
from .recruit_company import CompanyCrawling
import re
import requests
from bs4 import BeautifulSoup

wordDic = {}

def crawling():
    site = 'programmers'
    for num in range(1950, 1950+1):
        url = f'https://programmers.co.kr/job_positions/{num}'
        responce = requests.get(url)
        soup = BeautifulSoup(responce.text, 'html.parser')
        is_recruit = soup.select(
            'body > div.main > div.position-show > div > div > \
                div.content-body.col-item.col-xs-12.col-sm-12.col-md-12.col-lg-8'
        )
        if not is_recruit:
            continue
        # 회사 정보 크롤링
        company = CompanyCrawling()
        company.crawling_compnay_all(soup)
        # 공고 정보 크롤링
        recruit = RecruitCrawling(index=num, url=url, site = site)
        recruit.crawling_recruit_all(soup)
        # 스택 크롤링
        stk = StackCrawling(num)
        stacks = stk.crawling_stack_all(soup)
        # 크롤링한 데이터 DB인젝션
        model_crud.data_into_db(company,recruit,stacks)

    model_crud.detail_null_stack()