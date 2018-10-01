from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from . import models

def index(request):
    article = models.Article.objects.get(pk=1)
    return render(request,'index.html',{'article':article})
    # return HttpResponse('hello,world!')