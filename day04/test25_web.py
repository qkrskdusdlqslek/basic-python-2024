# file : test25_web.py
# desc : urllib(urllibrary) 모듈 사용법
# 웹 사이트 내용을 파이썬으로 가져오는 것

# from urllib.request import * request 모듈안의 모든 내용 다 사용할 때
from urllib.request import Request, urlopen  # Request 클래스와 urlopen만 쓰겠다

req = Request('https://www.naver.com/') # 네이버 웹주소(url) / Request는 클래스
res= urlopen(req) # url주소로 웹사이트 열어달라고 요청

print(f'응답코드 : {res.status}') # url로 요청된 웹사이트 응답 확인
print(res.read())

# urllib.request보다 조금 더 성능이 나은 모듈
import requests

res2 = requests.get('https://www.naver.com/') # requests는 함수

print(res2.status_code)
print(res2.text) 













