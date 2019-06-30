from django.db import models

# Create your models here. 实体类
class Task(models.Model):

    name = models.CharField(null=False,max_length=32)
    user = models.CharField(null=False,max_length=32)
    active = models.IntegerField(default=0,max_length=2)
