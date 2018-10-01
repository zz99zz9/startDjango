from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from . import models

def index(request):
    articles = models.Article.objects.all()
    return render(request,'index.html',{'articles':articles})
    # return HttpResponse('hello,world!')

def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'article_page.html',{'article':article})