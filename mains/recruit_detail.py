import re


class RecruitCrawling:
    def __init__(self, index, url, site):
        # self.company_id = company_id
        self.index = index
        self.title = None
        self.job = None
        self.carear_start = None
        self.carear_end = None
        self.url = url
        self.site = site
        # 게시일은 그냥 크롤링한 날자 그대로 넣자.

    def crawling_recruit_all(self, soup):
        self.crawling_recruit_title(soup)
        self.crawling_recruit_job(soup)
        self.crawling_recruit_carear(soup)

    def crawling_recruit_title(self, soup):
        recruit_title = soup.select(
            'body > div.main > div.position-show > div > header > \
            div.header-body.col-item.col-xs-12.col-sm-12.col-md-12.col-lg-8 > h2'
        )
        self.title = re.sub("\n", "", recruit_title[0].get_text('h2')).strip()

    def crawling_recruit_job(self, soup):
        recruit_position = soup.select(
            'section.section-summary > table > tbody > tr:nth-child(1) > td.t-content'
        )
        self.job = recruit_position[0].get_text('td')

    def crawling_recruit_carear(self, soup):
        recruit_carear = soup.select(
            'section.section-summary > table > tbody > tr:nth-child(2) > td.t-content'
        )
        carear_text = recruit_carear[0].get_text('td')

        if(carear_text == '경력 무관'):
            recruit_carear_start = 0
            recruit_carear_end = 10
        elif(carear_text == '신입'):
            recruit_carear_start = 0
            recruit_carear_end = 0
        else:
            recruit_carear_start, recruit_carear_end = carear_text.split('~')
            recruit_carear_start = int(recruit_carear_start.strip())
            recruit_carear_end = int(re.sub(
                "[^0-9]", "", recruit_carear_end.strip()))

        self.carear_start = recruit_carear_start
        self.carear_end = recruit_carear_end
