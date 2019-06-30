#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mydjango.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)

# 和manage.py同一级目录执行
# python manage.py startapp blog

# migrations 数据迁移模块
# admin.py 后台管理系统配置
# apps.py 当前应用的一些配置。没什么意思
# models.py 数据模块 （ORM）
# test.py 自动化测试，测试脚本
# views.py 执行响应的逻辑代码（重要）

# python manage.py runserver 9090 修改端口号