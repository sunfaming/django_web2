from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 创建了一个名为Topic 的类，它继承Model ，即Django中定义了模型基本功能的类


class Topic(models.Model):
# 用户学习的主题。
# 给Topic 类添加了两个属性：text 和date_added
# 属性text 是一个CharField ——由字符组成的数据
    text = models.CharField(max_length=200)
# 属性date_added 是一个DateTimeField ——记录日期和时间的数据
    date_added = models.DateTimeField(auto_now_add=True)
# 添加一个关联到用户的外键
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
# Django调用方法__str__() 来显示模型的简单表示。
# 方法__str__() ，它返回存储在属性text 中的字符串
    def __str__(self):
        return self.text
    
# 返回模型的字符串表示。
class Entry(models.Model):
# 学到的有关某个主题的具体知识。
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'entries'
    # class Meta:
		# verbose_name_plural = 'entries'
    def __str__(self):
    # 返回模型的字符串表示。
        if len(self.text[:])<50:
            return self.text
        else:
            return f"{self.text[:50]}..."


    
