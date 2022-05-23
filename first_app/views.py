from re import A
import re
from unittest import result
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

articles={
    'sports':'Sports Page',
    'finance':'Finance Page',
    'politics':'Politics Page',
    
}

# def politics_views(request):
#     return HttpResponse(articles['politics'])

# def sports_views(request):
#     return HttpResponse(articles['sports'])

# def finance_views(request):
#     return HttpResponse(articles['finance'])

def  news_views(request,topic):
    try:
        result=articles[topic]
        return HttpResponse(result)
    except:
        result="No page for that topic!"
        return HttpResponseNotFound(result)

def add_view(request,n1,n2):
    s=n1+n2
    return HttpResponse(str(s))


