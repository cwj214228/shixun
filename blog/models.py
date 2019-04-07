from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNum
from read_statistics.models import ReadNumExpandMethod

# Create your models here.


class Ranking(models.Model):
    title=models.CharField(max_length=100,default='标题')
    content=models.TextField(null=True)

    def __str__(self):
        return self.title

class ArticleType(models.Model):
    type_name=models.CharField(max_length=15)
    def __str__(self):
        return self.type_name

# 这个类继承了两个东西
class Articles(models.Model,ReadNumExpandMethod):
    title=models.CharField(max_length=50,null=False)
    ArticleType=models.ForeignKey(ArticleType,on_delete=models.DO_NOTHING)
    content=RichTextUploadingField()
    author=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    created_time=models.DateTimeField(auto_now_add=True)
    Praise=models.IntegerField(default=0) #点赞数
    def __str__(self):
        return self.title








#python manage.py makemigrations   生成迁移脚本文件
#python manage.py migrate 把新生成的迁移脚本文件映射到数据库中