from flask import Flask, request, render_template
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openai
import os
import sys
import json
import urllib.request
import re

app = Flask(__name__) 


# 이건 제 네이버 api 여서 바꿔서 쓰세요
client_id = "0At29T7vkcGGyngOl5BY"
client_secret = "DJShkQKQXe"


# 기본 루트 경로에 대한 라우트 설정
@app.route('/', methods=['GET', 'POST'])


def index():
    if request.method == 'POST':
        # HTML 폼에서 'text' 필드에서 데이터를 가져옵니다.
        keyword = request.form['input_data']
        encText = urllib.parse.quote(keyword) 

        url = "https://openapi.naver.com/v1/search/news?query=" + encText  # JSON 결과 뉴스검색
        # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
        news = urllib.request.Request(url)
        news.add_header("X-Naver-Client-Id", client_id)
        news.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(news)

        rescode = response.getcode()
        if rescode == 200:
            response_body = response.read()
            newsdata = response_body.decode("utf-8")
            newsdatas = json.loads(newsdata)
            
            links = [item['link'] for item in newsdatas['items']]       #링크

            naver_links = [link for link in links if 'naver.com' in link]
            n_link = naver_links[0]
            
        
        else:
            print("Error Code:" + rescode)
        
        # url 입력받아 기사 본문 크롤링
        html = urlopen(n_link)
        bs = BeautifulSoup(html.read(), 'html.parser')

        text = bs.find('article', {'id':'dic_area'}).get_text()
        text = text.split('기자 = ')[-1]
        

        
        # 챗GPT
        openai.api_key = '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' # api key 입력
        
        
        #요약
        messages=[]
        content = f"'{text}'를 간략히 요약해줘"
                
        # 질문 저장
        messages.append({"role":"user", "content":content})
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        chat_response = completion.choices[0].message.content
        
        # 대답 저장
        messages.append({"role":"assistant", "content":chat_response})


        #원문 영어 번역
        messages=[]
        content1 = f"'{text}'를 영어로 번역해줘"
                
        # 질문 저장
        messages.append({"role":"user", "content":content1})
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        chat_response2 = completion.choices[0].message.content
        
        # 대답 저장
        messages.append({"role":"assistant", "content":chat_response2})





        #요약 영어 번역
        messages=[]
        translate = f"'{chat_response}'를 영어로 번역해줘"
         # 질문 저장
        messages.append({"role":"user", "content":translate})
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        chat_response1 = completion.choices[0].message.content
        # 대답 저장
        messages.append({"role":"assistant", "content":chat_response1})
        
        
        
        
        
        
        
        
        return render_template('index.html', text=text, summary=chat_response,summary1=chat_response1,summary2=chat_response2, ori_url=n_link)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)