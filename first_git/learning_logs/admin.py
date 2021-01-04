from django.contrib import admin

# Register your models here.
# models 前面的句点让Django在admin.py所在的目录中查找models.py
from .models import Topic, Entry
# admin.site.register() 让Django通过管理网站管理模型
admin.site.register(Topic)
admin.site.register(Entry)