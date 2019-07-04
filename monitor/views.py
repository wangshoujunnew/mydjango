from django.shortcuts import render
from django.http import HttpResponse
from monitor.models import *
from util.logger import *
from util.crontabUtil import *
# Create your views here.
logger = getLooger()

def index(request): # url的分发需要传递一个request对象
    obj = {
        "name":"shoujunw",
        "age":10
    }

    c = CrontabUtil()
    # print(c.comCronNow("0 8 * * *"))

    for task in Task.objects.all():
        print('task -------- ')
        crontab = task.crontab
        name = task.name
        print('name: {}'.format(name))
        need,time = c.comCronNow(crontab)
        print(time)
        if need:
            print("去数据库中检查标记文件")
            if checkTaskRec(name,time):
                logger.info('ok')
            else:
                logger.warn('send Message to User for Warning')
        else:
            print('no need')



    return HttpResponse(str(obj))

def checkTaskRec(name,recTime):
    """
    检查记录
    记录的任务名称
    大于某个时间recTime的记录
    记录的条数>0
    """
    isOk = False
    for rec in TaskRec.objects.filter(taskName=name):
        if rec.lastGeneTime >= recTime:
            isOk = True
            break
    return isOk

def dbShow(request): # 数据库记录
    logger.info('dbShow run ...')
    all = Task.objects.all()

    task = Task()
    task.user = 'sjw'
    task.name = 'hello2'
    task.active = 1
    # task.save()

    print(all[0])
    return HttpResponse(','.join(list(map(lambda e:e.name,all))))

def paramParse(request,name):
    logger.info(name)
    return HttpResponse('success')

def paramJSON(request):
    json = request.GET.get('json','no json')
    logger.info(json)
    return HttpResponse('success')

