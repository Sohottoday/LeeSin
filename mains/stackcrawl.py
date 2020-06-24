import requests
import urllib.request
from bs4 import BeautifulSoup

# 'Visual Studio Code' 는 visual-studio-code
# 'Node.js' 는 Nodejs
stacklist = ['JavaScript','Visual Studio Code','Node.js']
for item in stacklist:

    item=item.replace(" ","-")
    item=item.replace(".","")
    
    url = f'https://stackshare.io/{item}'
    
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'html.parser')
    
    link = soup.select(
        'div.css-mgyi0p > div.css-ii8qy4 > div.css-12i35kv > div.css-1vc2fh0 > div > a'
    )

    # print(link[0].get('href'))

    # stackresponce = requests.get(link[0].get('href'))
    # stacksoup = BeautifulSoup(stackresponce.text, 'html.parser')

    # 스킬 설명 크롤링
    imgSelect = soup.select(
        'img'
    )

    imgURL=imgSelect[0].get('src')
    
    urllib.request.urlretrieve(imgURL, imgURL.split("/")[-1])
    # print(imgURL.split("/")[-1])

    