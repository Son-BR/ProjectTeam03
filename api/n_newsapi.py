
# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request

#client_id = "YOUR_CLIENT_ID"
#client_secret = "YOUR_CLIENT_SECRET"
client_id = "0At29T7vkcGGyngOl5BY"
client_secret = "DJShkQKQXe"

encText = urllib.parse.quote("Chat GPT")  #  " "에 검색할 입력값
url = "https://openapi.naver.com/v1/search/news?query=" + encText # JSON 결과 뉴스검색
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)


# 출처 : https://developers.naver.com/docs/serviceapi/search/blog/blog.md