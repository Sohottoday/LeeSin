# from PyKomoran import *
import re
from . import model_crud


class StackCrawling:
    def __init__(self, recruitID):
        self.recruitID = recruitID

    # 밑에 매서드 전부 실행, 및 추출된 단어로 딕셔너리 생성
    def crawling_stack_all(self, soup):
        requriedDic = self.crawling_requried(soup)
        preferenceDic = self.crawling_preference(soup)
        positionDic = self.crawling_position(soup)
        # 기술 스택을 저장해 주기 위해서라도 필요하다.
        stackDic = self.crawling_stack(soup)
        stackDic = {**stackDic, **requriedDic, **preferenceDic, **positionDic}
        return stackDic

    # 자격 사항 크롤링
    def crawling_requried(self, soup):
        required = soup.select(
            'div.content-body.col-item.col-xs-12.col-sm-12.col-md-12.col-lg-8 > \
                section.section-requirements > div > div > ul > li'
        )
        wordDic = {}
        for item in required:
            reDic = self.morphological_analysis(item.get_text('li'))
            wordDic = {**wordDic, **reDic}
        return wordDic

    # 우대조건 크롤링
    def crawling_preference(self, soup):
        preference = soup.select(
            'div.content-body.col-item.col-xs-12.col-sm-12.col-md-12.col-lg-8 > \
                section.section-preference > div > div > ul > li'
        )
        wordDic = {}
        for item in preference:
            reDic = self.morphological_analysis(item.get_text('li'))
            wordDic = {**wordDic, **reDic}
        return wordDic

    # 업무소개 크롤링
    def crawling_position(self, soup):
        position = soup.select(
            'div.content-body.col-item.col-xs-12.col-sm-12.col-md-12.col-lg-8 > \
                section.section-position > div > div > ul > li'
        )
        wordDic = {}
        for item in position:
            # print(item)
            reDic = self.morphological_analysis(item.get_text('li'))
            wordDic = {**wordDic, **reDic}
        return wordDic

    # 기술 스택 크롤링
    def crawling_stack(self, soup):
        stacks = soup.select(
            'section.section-stacks > table > tbody > tr > td > code'
        )
        stackDic = {}
        for item in stacks:
            name = item.get_text('li')
            if '(' in name:
                name = re.sub(")","",name.split('(')[1])
            model_crud.find_stack(name)
            stackDic[name] = True
        return stackDic

    # 전처리 함수
    def morphological_analysis(self, plain_text):
        wordDic = {}
        plain_text = plain_text.replace(u'\xa0', u' ')
        # plain_text = re.sub("[가-힣():]", "", plain_text).strip()
        plain_text = re.sub("[가-힣]", "", plain_text).strip()
        plain_text = re.sub("[ ]+", " ", plain_text).strip()
        # plain_text = plain_text.encode("utf-8")
        some_row_text = plain_text.split(", ")
        # print(some_row_text)
        for item in some_row_text:
            split2_row = re.split('[)(/)]', item)
            for element in split2_row:
                if not element:
                    continue
                reDic = model_crud.check_item_in_model(element.strip())
                wordDic = {**wordDic, **reDic}
        return wordDic
