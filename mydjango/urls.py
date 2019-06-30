"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

# 导入view的函数
from monitor.views import *

urlpatterns = {
    url(r'^admin/', admin.site.urls),
    # 配置url, 进行url分发
    url(r'monitor/index', view=index),
    url(r'monitor/dbShow', view=dbShow),
    # 直接通过http://localhost:9090/monitor/paramParse/shoujunw的方式传递参数
    url(r'monitor/paramParse/(\w+)$', view=paramParse),
    url(r'monitor/paramJSON', view=paramJSON),
}
