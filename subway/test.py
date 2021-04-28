import requests
from google.cloud import firestore #firestore client lib
#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import db
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
db = firestore.Client()
for tag in result.find_all('item'):
    doc_ref = db.collection('지하철')
    doc_ref.add(tag.text)
    i=i+1

if __name__ == "__main__":
    main()