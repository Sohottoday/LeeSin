from .recruit_company import CompanyCrawling
from .recruit_detail import RecruitCrawling
from .recruit_stack import StackCrawling
import requests
from bs4 import BeautifulSoup
import re

wordDic = {}

def crawling():
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
        # 회사 정보 크롤링
        company = CompanyCrawling()
        company.crawling_compnay_all(soup)
        
        # 공고 정보 크롤링
        recruit = RecruitCrawling(index=num, url=url)
        recruit.crawling_recruit_all(soup)

        sc = StackCrawling(num)
        # 200까지함
        sc.crawling_stack(soup)
            
        requriedDic = sc.crawling_requried(soup)
        preferenceDic = sc.crawling_preference(soup)
        positionDic = sc.crawling_position(soup)
        
        stackDic = {**requriedDic, **preferenceDic, **positionDic}
        

        