import requests
from bs4 import BeautifulSoup
import json
import sys
from re import sub
import datetime

url = "http://data.humetro.busan.kr/voc/api/open_api_distance.tnn?act=xml&numOfRows=229&serviceKey=HjmUTLQhRVX8z0M7dGyySaa8VubQR%2B2X0arwiUO3KBdTZo9YCQoxSxhke0pjTLJSfZec%2FYQp2aO%2F1lRu6saO%2FA%3D%3D"

result = {}
request = requests.get(url)#url의 페이지를 로딩해 저장
html = request.text
soup = BeautifulSoup(html, "html.parser")

for tag in soup.find_all("item"):
    station = soup.find("startsn").string.strip()
    interval = soup.find("time").string.strip()
    exchange = soup.find("exchange").string.strip()
    stoppingtime = soup.find("stoppingtime").string.strip()
    result["station"] = station
    result["interval"] = interval
    result["exchange"] = exchange
    result["stoppingtime"] = stoppingtime

print(result)

