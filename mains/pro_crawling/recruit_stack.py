# from PyKomoran import *
import re

class StackCrawling:
    # komoran = Komoran("EXP")

    def __init__(self, recruitID):
        self.recruitID = recruitID
        self.preferencelist = []
        self.requiredlist = []
        self.stacklist = []

    # 자격 사항 크롤링
    def crawling_requried(self, soup):
        required = soup.select(
            'div.content-body.col-item.col-xs-12.col-sm-12.col-md-12.col-lg-8 > section.section-requirements > div > div > ul > li'
        )

        for item in required:
            self.morphological_analysis(item.get_text('li'))
            # print(item.get_text('li'))
            # self.requiredlist.append(item.get_text('li'))

    # 우대조건 크롤링
    def crawling_preference(self, soup):
        preference = soup.select(
            'div.content-body.col-item.col-xs-12.col-sm-12.col-md-12.col-lg-8 > \
                section.section-preference > div > div > ul > li'
        )

        for item in preference:
            print(item.get_text('li'))
            # self.preferencelist.append(item.get_text('li'))

    # 기술 스택 크롤링
    def crawling_preference(self, soup):

        stacks = soup.select(
            'section.section-stacks > table > tbody > tr > td > code'
        )

        for item in stacks:
            # item = re.sub(".","",item)
            print(item.get_text('li'))
            # self.stacklist.append(stack.get_text('code'))

    # 전처리 함수
    def morphological_analysis(self, plain_text):
        print(plain_text)
        plain_text = plain_text.replace(u'\xa0', u' ')
        plain_text = re.sub("[가-힣():]", "", plain_text).strip()
        plain_text = re.sub("[ ]+", " ", plain_text).strip()
        # plain_text = plain_text.encode("utf-8")
        some_row_text = plain_text.split(", ")
        print(some_row_text)
        print("""\n""")


        # morpheme_list = komoran.get_list(plain_text)
        # SL_list = []
        # # print(morpheme_list)
        # for morpheme in morpheme_list:
        #     if 'SL' in morpheme.get_second():
        #         SL_list.append(morpheme.get_first())

        # for i in range(SL_list):
            
        #     pass
            # 만약 데이터베이스 안에 그 단어가 like
            # 1개면 그냥 SL과 완전 일치하는지 찾고 넣는다.
            # 2개 이상이면 그 다음 것까지 묶고 다시 검색
            # 그 다음 것과 묶어서 완전 일치하는거 있는지 찾음.
            # 있으면 그것까지 묶어서 스택에 추가
            # 없으면 첫번째 단어와 완전일치 찾고 스택에 추가
            # print(SL)
