import logging
from logging.handlers import TimedRotatingFileHandler

def getLooger(path='log'):
    debug = True
    # 日志输出格式
    # %(levelno)s: 打印日志级别的数值
    # %(levelname)s: 打印日志级别名称
    # %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
    # %(filename)s: 打印当前执行程序名
    # %(funcName)s: 打印日志的当前函数
    # %(lineno)d: 打印日志的当前行号
    # %(asctime)s: 打印日志的时间
    # %(thread)d: 打印线程ID
    # %(threadName)s: 打印线程名称
    # %(process)d: 打印进程ID
    # %(message)s: 打印日志信息
    log_format = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
    if debug:  # 如果是调试模式的话,就在屏幕上也打印出来
        logging.basicConfig(level=logging.DEBUG,
                            format=log_format)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # (日志滚动,过期删除) 每天产生一个文件
    # 创建TimedRotatingFileHandler对象
    # interval: 滚动周期，单位有when指定，比如：when=’D’,interval=1，表示每天产生一个日志文件
    # when=M: 每分钟保存一个日志文件
    # backupCount: 表示日志文件的保留个数
    log_file_handler = TimedRotatingFileHandler(filename= path + "/log", when="D", interval=1, backupCount=2)

    log_file_handler.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
    log_file_handler.setFormatter(logging.Formatter(log_format))
    logger.addHandler(log_file_handler)

    return logger
