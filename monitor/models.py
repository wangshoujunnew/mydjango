from django.db import models

# Create your models here. 实体类
class Task(models.Model):
    """任务"""
    name = models.CharField(null=False,max_length=32)
    user = models.CharField(null=False,max_length=32)
    crontab = models.CharField(null=False,max_length=32)
    generateFile = models.CharField(null=False,max_length=32)
    active = models.IntegerField(default=0,max_length=2)

    @staticmethod
    def init(param): # name,user,active
        task = Task()
        task.name,task.user,task.crontab,task.generateFile,task.active = param
        return task


class TaskRec(models.Model):
    """任务记录"""
    taskName = models.CharField(null=False,max_length=32)
    taskCount = models.IntegerField(default=0,max_length=10) # 这是第几次task
    lastGeneTime = models.CharField(null=False,max_length=32) # task的任务完成时间
    wc_l = models.IntegerField(default=0,max_length=10) # 文件行数


# 记录操作
# insert
# Author.objects.create(first_name='fe',last_name='cow', email='280773872@qq.com')
# select
# Author.objects.filter(last_name='cu_cow')
# 返回一个对象
#  author = Author.objects.get(id=1)