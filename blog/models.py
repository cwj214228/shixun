from django.db import models

# Create your models here.
class Artical(models.Model):
    title=models.CharField(max_length=100,default='标题')
    content=models.TextField(null=True)

    def __str__(self):
        return self.title

class Ranking(models.Model):
    title=models.CharField(max_length=100,default='标题')
    content=models.TextField(null=True)

    def __str__(self):
        return self.title


#python manage.py makemigrations   生成迁移脚本文件
#python manage.py migrate 把新生成的迁移脚本文件映射到数据库中