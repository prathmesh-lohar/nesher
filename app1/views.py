from django.shortcuts import render
import requests
import os
import json
# Create your views here.


def home(request):
    url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=826f05f00a2847738c60df0260a8691b')
    response = requests.get(url)
    data = response.json()

    articles = data['articles']

    context = {
        'data':data,
        'articles':articles,
    }

    
    return render(request,"home.html",context)