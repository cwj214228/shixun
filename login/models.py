from django.db import models


# Create your models here.
class Userlist(models.Model):
    username=models.CharField(max_length=30,null=False)
    password=models.CharField(max_length=30,null=False)

    def __str__(self):
        return "<Userlist:({username},{password})>".format(username=self.username,password=self.password)

#python manage.py makemigrations   生成迁移脚本文件
#python manage.py migrate 把新生成的迁移脚本文件映射到数据库中