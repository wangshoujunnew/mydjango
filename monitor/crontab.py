# monitorApp下的定时任务
from monitor.models import *
from util.crontabUtil import *
from util.logger import *
logger = getLooger()

def showHello():
    print('hello ')

# 每隔2分钟去数据库里面扫描一遍是否有新的任务应该生成了

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

def checkTask():
    c = CrontabUtil()
    # print(c.comCronNow("0 8 * * *"))
    for task in Task.objects.all():
        print('task -------- ')
        crontab = task.crontab
        name = task.name
        print('name: {}'.format(name))
        need, time = c.comCronNow(crontab)
        print(time)
        if need:
            print("去数据库中检查标记文件")
            if checkTaskRec(name, time):
                logger.info('ok')
            else:
                logger.warn('send Message to User for Warning')
        else:
            print('no need')
