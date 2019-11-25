'''
案例实践

1. 需求

现在对日志的记录有以下几个要求

    1) 要求将所有级别的所有日志都写入到磁盘中
    2) all.log文件中记录所有的日志信息, 日志格式为: 日期和时间 - 日志级别 - 日志信息
    3) error.log文件中单独建记录 error 及以上级别的日志信息, 日志格式为 日期和时间 - 日止级别 - 文件名[:行号] 日志信息
    4) 要求 all.log 在每天凌晨进行日志切割

2. 分析

    1) 要记录所有几倍的日志, 因此日志器的有效 level 需要设置最低级别 - DEBUG
    2) 日志需要被发送到两个不同的目的地, 因此需要为日志器设置两个 Handler; 另外, 两个目的地都是磁盘文件, 因此两个 Handler 都是与File
    3) all.log 要求按照时间进行日志分割, 因此小勇 logging.handler.TimeRotation; 而 error.log 没有要求日志分隔
    4) 两个日志文件的格式不同, 因此需要对这两个 handler 分别进行设置格式器
'''

import logging
import logging.handlers
import datetime

# 定义 logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)


# 为两个不同的文件设置不同的 handler
rf_handler = logging.handlerlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backCount=7, at)
rf_handler.setFormat(logging,Formatter("%(asctime)s - %(levelname)s - %(message)s"))



f_handler = logging.FileHandler('error.log')
f_handler.setlevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

# 把相应的处理器组装到 logger 上
logger.addHandler(rf_handler)
logger.addHandler(f_handler)


logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
