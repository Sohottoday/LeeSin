import re


class CompanyCrawling:
    def __init__(self):
        self.compnay_name = None
        self.compnay_scale = None
        self.compnay_homepage = None

    # 회사 이름 크롤링
    def crawling_compnay_name(self, soup):
        comName = soup.select(
            'header > div.header-body.col-item.col-xs-12.col-sm-12.col-md-12.col-lg-8 > h4'
        )

        self.compnay_name = comName[0].get_text('h4')

    # 회사 규모(인원) 크롤링
    def crawling_compnay_scale(self, soup):

        comScale = soup.select(
            'section.section-summary > table > tbody > tr:nth-child(3) > td.t-content'
        )

        self.compnay_scale = re.sub("[^0-9]", "", comScale[0].get_text('td'))

    # 회사 홈페이지 크롤링
    def crawling_compnay_scale(self, soup):

        comhomepage = soup.select(
            'div.content-side.col-item.col-xs-12.col-sm-12.col-md-12.col-lg-4 > section > ul > li:nth-child(1) > h6.list-value > a'
        )

        self.compnay_homepage = comhomepage[0].get('href')
