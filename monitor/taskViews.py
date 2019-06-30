from django.shortcuts import render
from django.http import HttpResponse
from monitor.models import *
from util.logger import *
import json
# Create your views here.
logger = getLooger()

def saveTask(request):
    task = request.GET.get('task',None)
    print(task)
    try:
        print(list(eval(task).values()))
        Task.init(list(eval(task).values())).save()
        logger.info('add task {}'.format(task))
        return HttpResponse('success')
    except Exception as e:
        logger.error(e)
        return HttpResponse(e)




