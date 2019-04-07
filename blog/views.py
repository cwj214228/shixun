from django.shortcuts import render, get_object_or_404
from django.shortcuts import render,redirect,reverse
from django.contrib import auth
# Create your views here.
from . import models
from .models import Articles
from django.contrib.contenttypes.models import ContentType
from read_statistics.models import ReadNum

def index(request):
    articles=models.Articles.objects.all()
    Ranking=models.Ranking.objects.all()
    return render(request,'Blog/index.html',{'articles':articles,'Ranking':Ranking})

# def Notice(request,article_id):
#     article=models.Articles.objects.get(title=article_id)
#     return render(request,'Blog/info.html',{'article':article})

def ranking(request,article_id):
    ranking = models.Ranking.objects.get(title=article_id)
    return render(request,'Blog/info.html',{'ranking':ranking})

def Artical_detail(request,Artical_pk):
    artical = models.Articles.objects.get(pk=Artical_pk)
    # 如果这个cookie已经存在，那就不会进行+1操作
    if not request.COOKIES.get('artical_%s_read' % Artical_pk):
        ct = ContentType.objects.get_for_model(artical)
        # 判断这篇文章的阅读数量是否为空
        if ReadNum.objects.filter(content_type=ct,object_id=artical.pk).count():
            # 获取对应的文章的对象
            readnum=ReadNum.objects.get(content_type=ct,object_id=artical.pk)
        else:
            # 创建一个新的对象，对象的文章就是上面对应的文章
            readnum=ReadNum(content_type=ct,object_id=artical.pk)
        readnum.read_num+=1
        readnum.save()

    response = render(request,'Blog/info.html',{'articals':artical})
    # 设置一个表示已经阅读了的cookie
    response.set_cookie('artical_%s_read'%Artical_pk,'true')

    return response
