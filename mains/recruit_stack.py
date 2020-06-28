# from PyKomoran import *
import re
from . import model_crud


class StackCrawling:
    # komoran = Komoran("EXP")

    def __init__(self, recruitID):
        self.recruitID = recruitID

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
        for item in stacks:
            model_crud.insert_stack(item.get_text('li'))

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
