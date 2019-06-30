from django.shortcuts import render
from django.http import HttpResponse
from monitor.models import *
from util.logger import *
# Create your views here.
logger = getLooger()

def index(request): # url的分发需要传递一个request对象
    obj = {
        "name":"shoujunw",
        "age":10
    }
    return HttpResponse(str(obj))

def dbShow(request): # 数据库记录
    logger.info('dbShow run ...')
    all = Task.objects.all()
    return HttpResponse(','.join(list(map(lambda e:e.name,all))))

def paramParse(request,name):
    logger.info(name)
    return HttpResponse('success')

def paramJSON(request):
    json = request.GET.get('json','no json')
    logger.info(json)
    return HttpResponse('success')

