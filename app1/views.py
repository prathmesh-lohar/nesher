from django.shortcuts import render
import requests
import os
import json
from gnewsclient import gnewsclient
# Create your views here.


def home(request):

    client = gnewsclient.NewsClient(language='english',
                                location='india',
                                topic='World',
                                use_opengraph=True,
                                max_results=20)
 
    news_list = client.get_news()
    print(news_list)
    context = {
        'news_list':news_list,
    }
    return render(request,"base.html",context)