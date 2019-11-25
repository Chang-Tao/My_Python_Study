import logging

LOG_FORMAT = "%(asctime)s======%(levelname)s++++++%(messsage)s"
logging.basicConfig(filename="lingsha.log",level=logging.DEBUG,format=LOG_FORMAT)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning.log")
logging.error("This is a error.log")
logging.critical("This is a critical.log")

# 另外一种写法
logging.log(logging.debug,"This is a debug log.")
logging.log(logging.info,"This is a info log.")
logging.log(logging.warning,"This is a warning.log")
logging.log(logging.error,"This is a error.log")
logging.log(logging.critical,"This is a critical.log")