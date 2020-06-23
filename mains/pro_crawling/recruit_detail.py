import re


class RecruitCrawling:
    def __init__(self, index, url, company_id):
        self.company_id = company_id
        self.index = index
        self.job = None
        self.carear_start = None
        self.carear_end = None
        self.url = url
        # 게시일은 그냥 크롤링한 날자 그대로 넣자.

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
            recruit_carear_start = recruit_carear_start.strip()
            recruit_carear_end = re.sub(
                "[^0-9]", "", recruit_carear_end.strip())

        self.carear_start = recruit_carear_start
        self.carear_end = recruit_carear_end
