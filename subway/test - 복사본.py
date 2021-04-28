import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from bs4 import BeautifulSoup

url = 'http://data.humetro.busan.kr/voc/api/open_api_distance.tnn?act=xml&numOfRows=229&serviceKey=HjmUTLQhRVX8z0M7dGyySaa8VubQR%2B2X0arwiUO3KBdTZo9YCQoxSxhke0pjTLJSfZec%2FYQp2aO%2F1lRu6saO%2FA%3D%3D'

#firebase DB 인증, 초기화 : in case realtime-DB
#cerd = credentials.Certificate('myKey.json')
#firebase_admin.initialize_app(cerd, {
#    'databaseURL' : 'https://subway-db-test1-default-rtdb.firebaseio.com/'
#})



result = requests.get(url)
soup = BeautifulSoup(result.content, "html.parser")

i=0
result = soup
for tag in result.find_all('item'):
    ref = db.reference('지하철/'+str(i))
    i=i+1
    ref.update({'시작역' : tag.text})