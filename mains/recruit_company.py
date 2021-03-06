import re


class CompanyCrawling:
    def __init__(self):
        self.name = None
        self.scale = None
        self.homepage = None

    def crawling_compnay_all(self, soup):
        self.crawling_compnay_name(soup)
        self.crawling_compnay_scale(soup)
        self.crawling_compnay_homepage(soup)

    # 회사 이름 크롤링
    def crawling_compnay_name(self, soup):
        comName = soup.select(
            'header > div.header-body.col-item.col-xs-12.col-sm-12.col-md-12.col-lg-8 > h4'
        )
        self.name = comName[0].get_text('h4')

    # 회사 규모(인원) 크롤링
    def crawling_compnay_scale(self, soup):
        comScale = soup.select(
            'section.section-summary > table > tbody > tr:nth-child(3) > td.t-content'
        )
        # print(comScale[0].get_text('td'))
        self.scale = int(re.sub("[^0-9]", "", comScale[0].get_text('td')))

    # 회사 홈페이지 크롤링
    def crawling_compnay_homepage(self, soup):
        comhomepage = soup.select(
            'div.content-side.col-item.col-xs-12.col-sm-12.col-md-12.col-lg-4 > \
                section > ul > li:nth-child(1) > h6.list-value > a'
        )
        self.homepage = comhomepage[0].get('href')
