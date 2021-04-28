import requests
from bs4 import BeautifulSoup
import json
import sys
from re import sub
import datetime

url = "http://data.humetro.busan.kr/voc/api/open_api_distance.tnn?act=xml&numOfRows=229&serviceKey=HjmUTLQhRVX8z0M7dGyySaa8VubQR%2B2X0arwiUO3KBdTZo9YCQoxSxhke0pjTLJSfZec%2FYQp2aO%2F1lRu6saO%2FA%3D%3D"

def crawler(asset_manager, url):
    try :
        r = requests.get(url)#url의 페이지를 로딩해 저장
        html = r.text
        soup = BeautifulSoup(html, "html.parser")
        aum_pre = soup.find('startSn')
        result = {}
        result["aum_pre"] = aum_pre
        return json.dumps(result)


    except Exception as e:
        print("Error occured", e)
        pass
