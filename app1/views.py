from django.shortcuts import render
import requests
import os
import json
from GoogleNews import GoogleNews

# Create your views here.

def home(request):


    url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=826f05f00a2847738c60df0260a8691b')
    response = requests.get(url)
    data = response.json()
    articles = data['articles'] 

    googlenews = GoogleNews(lang='en', region='IN',period='7d')
    
    googlenews.get_news('breaking news')

    

    res = googlenews.results()[:25]

    

    context = {
       'articles':articles,
       'res':res,
       
    }
    return render(request,"base.html",context)