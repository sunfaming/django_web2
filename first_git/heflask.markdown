
- penenv
    - https://zhuanlan.zhihu.com/p/71598248 
# 安装flake8之后写代码的时候编辑器就会提示哪里出错
- 创建DJANGO
    - 安装  pip install Django==3.1.4
    - 新建app django-admin startproject project_name .  (# 点不能省略)
    - 迁移 （migrate）数据库   python manage.py migrate
    - runserver 查看项目的状态 python manage.py runserver
    - Django搭建创建应用程序所需的基础设施  python manage.py startapp app_name
    - 要获悉可在模型中使用的各种字段，请参阅Django Model Field Reference
- 定义模型 models.py
- 激活模型 settings.py
    - INSTALLED_APPS 
        - # 我的应用程序 
        - 'learning_logs',
    - 让Django修改数据库，使其能够存储与模型Topic 相关的信息 python manage.py makemigrations learning_logs
    - 应用这种迁移，让Django替我们修改数据库 python manage.py migrate
- 在Django中创建超级用户 python manage.py createsuperuser
    - admin_sun  123456
- 迁移模型Entry
    - 添加新模型后，需要再次迁移数据库
    - python manage.py makemigrations app_name
    - python manage.py migrate
    - 注册模型Entry 
        - admin.py
        - from .models import Topic, Entry
        - admin.site.register(Entry)
    - Django shell
        - 测试项目和排除故障
        - 前面给模型Entry 定义了属性topic 。这是一个ForeignKey 
- 映射URL
    - urls.py
    - path('', include('learning_logs.urls')),
    - 在文件夹learning_logs中再创建一个urls.py文件
    - """定义learning_logs的URL模式。"""
        # 导入了函数path ，因为需要使用它将URL映射到视图
        from django.urls import path
        # 句点让Python从当前urls.py模块所在的文件夹导入views.py
        from . import views
        # 变量app_name 让Django能够将这个urls.py文件同项目内其他应用程序中的同名文件区分开来
        app_name = 'learning_logs'
        # 变量urlpatterns 是一个列表，包含可在应用程序learning_logs 中请求的页面。
        urlpatterns = [
         # 主页
	        path('', views.index, name='index'),
        ]
    - view.py
        - 设置相对应的函数
    - 链接 URL 
    - @login_required 限制访问
    - settings.py

- pip install django-bootstrap4
    - settings.py
        - INSTALLED_APPS
            - # 第三方应用程序
            - 'bootstrap4',
- 命令freeze 让pip将项目中当前安装的所有包的名称都写入文件requirements.txt
    - pip freeze > requirements.txt
    - 指定Python版本
        - python --version
        - manage.py所在的文件夹中新建一个名为runtime.txt的文件
        - runtime.txt
            - python-3.8.5