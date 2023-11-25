from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .models import Post
from .serializers import PostBaseModelSerializer
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostBaseModelSerializer

# Create your views here.
@api_view()
def getcrawling(request):
    driver = webdriver.Chrome()
    url = 'https://www.instagram.com'
    driver.get(url)
    time.sleep(10)

    email = ''
    input_id = driver.find_element(By.NAME, "username")
    input_id.clear()
    input_id.send_keys(email)

    password = ''
    input_pw = driver.find_element(By.NAME, "password")
    input_pw.clear()
    input_pw.send_keys(password)
    input_pw.submit()

    time.sleep(5)

    search_url = 'https://www.instagram.com/dev_event_crawler/'
    driver.get(search_url)
    time.sleep(10)

    #링크 추출
    links_selector = 'x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._a6hd'
    links = driver.find_elements(By.CLASS_NAME, links_selector)
    print('link',len(links))
    time.sleep(10)

    #제목 추출
    title_selector = '_aagv'
    titles = driver.find_elements(By.CLASS_NAME, title_selector)
    print('title',len(titles))
    time.sleep(10)

    pattern = re.compile(r"https://www.instagram.com/p/.*")
    for i in range(len(links)):
        link = links[i].get_attribute("href")
        print(i, link)
        if pattern.match(link):
            img_element = titles[i-20].find_element(By.TAG_NAME, 'img')
            alt_text = img_element.get_attribute('alt')
            match = re.search(r"text that says '(.*?)'", alt_text)
            if match:
                save_title  = match.group(1)
            else:
                save_title  = '클릭 후 이동해서 확인해주세요!'
            Post.objects.create(title= save_title, url=link)
    
    driver.quit()

    data={
        'type' : 'FBV',
        'result' : 'finish crwaling',
        }
    return Response(data)
