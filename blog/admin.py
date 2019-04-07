from django.contrib import admin

# Register your models here.
from .models import Ranking,ArticleType,Articles


admin.site.register(Ranking)

@admin.register(ArticleType)
class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id','title','ArticleType','author','get_read_num','created_time','Praise')

'''
@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('Reading_volume','articles')
'''