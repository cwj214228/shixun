from django.contrib import admin

# Register your models here.
from .models import Artical,Ranking

admin.site.register(Artical)
admin.site.register(Ranking)