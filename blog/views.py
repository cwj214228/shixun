from django.shortcuts import render
from django.shortcuts import render,redirect,reverse
from django.contrib import auth
# Create your views here.
from . import models

def index(request):
    articles=models.Artical.objects.all()
    Ranking=models.Ranking.objects.all()
    return render(request,'Blog/index.html',{'articles':articles,'Ranking':Ranking})

def list(request):
    return render(request,'Blog/list.html')
