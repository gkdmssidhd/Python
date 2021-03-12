from pprint import pprint

import requests
from bs4 import BeautifulSoup

# 크롤링 하려는 웹사이트의 소스코드를 읽어 온다.

responce = requests.get("http://www.naver.com/")
assert responce.status_code is 200

# 앞에 b 붙어있는거 바이트 코드 respone확인
# pprint(responce.content)

# selector 객체를 생성
dom = BeautifulSoup(responce.content, "html.parser")
# print(dom)

# title_lis = dom.find_all("strong",class_="main_topic_title")
title_lis = dom.select("div.main_topic_content")
# for title in title_lis :
print(title_lis)

header = dom.select("div#header")
print(header)
