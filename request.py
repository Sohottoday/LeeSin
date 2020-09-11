import requests
import urllib.request
from bs4 import BeautifulSoup

urls = ["http://127.0.0.1:8000/mains"]
# urls = ["https://cordingtrend.azurewebsites.net/mains", "http://127.0.0.1:8000/mains"]
for url in urls:
    print(url + " - test")
    i = 1
    while True:
        try:
            i += 1
            responce = requests.get(url)
            soup = BeautifulSoup(responce.text, 'html.parser')
            is_in = soup.select("body > div > div > a")
            if not is_in:
                raise
            print("success!!")
            break
        except:
            if i == 10:
                print("Fail")
                exit()
            else:
                print("Retry")
    print(url + " - end")
    responce = requests.get(url + "/crawling")
    print(url + "/crawling - end")
    responce = requests.get(url + "/issue")
    print(url + "/issue - end")
    responce = requests.get(url + "/repository")
    print(url + "/repository, end")
    responce = requests.get(url + "/setting")
    print(url + "/setting - end")