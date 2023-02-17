from django.shortcuts import render
import requests
import os
import json
from gnewsclient import gnewsclient

# Create your views here.


def home(request):

    

    # url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=826f05f00a2847738c60df0260a8691b')
    # response = requests.get(url)
    # data = response.json()
    # articles = data['articles']

    client = gnewsclient.NewsClient(language='english',location='india',topic='sports',use_opengraph=True,max_results=4)
 
    news_list = client.get_news()

    context = {
       
        'news_list':news_list,
    }
    return render(request,"base.html",context)