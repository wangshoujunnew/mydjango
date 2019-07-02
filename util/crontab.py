# 定时任务
from croniter import croniter
from datetime import datetime


str_time_now=datetime.now()

iter=croniter("0 8 * * *",str_time_now)

print(iter.get_next(datetime))
# 打印结果为：2019-02-22 08:00:00

# 定时任务的4中选择
# 使用while创建一个死循环，判断时间，从而执行一些函数
# 使用APScheduler库实现定时任务 （详情可以见http://blog.csdn.net/hui3909/article/details/46652623）
# ** django-crontab实现定时任务 pip install django-crontab
# django-celery实现定时任务