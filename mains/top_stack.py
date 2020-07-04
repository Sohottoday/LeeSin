import requests
import urllib.request
from bs4 import BeautifulSoup

from .stack_crawl import Crawling_Stack
from .model_crud import find_stack
import time


class Top:
    def __init__(self, name):
        self.name = name
        self.img = None
        self.detail = None
        self.category = None
        self.webpage = None
        self.stackshare = None


def top_stack(num):
    url = f'https://stackshare.io/tools/top?page={num}'

    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'html.parser')

    inprintint = soup.select(
        '#service-name-trending'
    )

    top_stack = [Top(item.get_text('span')) for item in inprintint]

    detailsoup = soup.select(
        'div > div > div.trending-description'
    )

    for idx, item in enumerate(detailsoup):
        top_stack[idx].detail = item.get_text('div').strip()

    hompagesoup = soup.select(
        '#mobile-tools-link > a'
    )

    for idx, item in enumerate(hompagesoup):
        if idx % 2 == 1:
            continue
        top_stack[idx//2].webpage = item.get('href')

    categorysoup = soup.select(
        '#trending-box > div.mobile-tools-row > div.flex-item.mobile-description > div > div > ol > li'
    )

    for idx, item in enumerate(categorysoup):
        top_stack[idx].category = item.get_text(
            'span').strip().strip('span').replace('span\nspan', '\\')

    stacksharesoup = soup.select(
        '#trending-box > div.mobile-tools-row > div:nth-child(2) > a'
    )

    for idx, item in enumerate(stacksharesoup):
        top_stack[idx].stackshare = f'https://stackshare.io{item.get("href")}'

    stacksharesoup = soup.select(
        '#trending-box > div.mobile-tools-row > div:nth-child(2) > a > div > img'
    )

    for idx, item in enumerate(stacksharesoup):
        try:
            imgURL = item.get('src')
            if imgURL[-1] == '/':
                imgURL = imgURL[:-1]
            urllib.request.urlretrieve(
                imgURL, f'media/icon/{top_stack[idx].name}.{imgURL.split(".")[-1]}')
            top_stack[idx].img = f'icon/{top_stack[idx].name}.{imgURL.split(".")[-1]}'
        except:
            top_stack[idx].img = 'icon/dummy.png'

    for item in top_stack:
        print(item.name)
        stk = find_stack(item.name)
        stk.img = item.img
        stk.detail = item.detail
        stk.category = item.category
        stk.webpage = item.webpage
        stk.stackshare = f'https://stackshare.io/tools/top?page={item.name}'
        stk.save()
        time.sleep(1)