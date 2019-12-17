import time
import threading

def loop1(in1):
    # ctime 得到当前时间
    print("Start loop 1 at:", time.ctime())
    # 把参数打印出来
    print("我是参数", in1)
    # 睡眠时间, 单位是秒(s)
    time.sleep(4)
    print("End loop 1 at:", time.ctime())

def loop2(in1, in2):
    # ctime 得到当前时间
    print("Start loop 2 at:", time.ctime())
    # 把参数打印出来
    print("我是参数 ", in1, "和参数 ", in2)
    # 睡眠时间, 单位是秒(s)
    time.sleep(2)
    print("End loop 2 at:", time.ctime())


def main():
    print("Starting at:", time.ctime())

    t1 = threading.Thread(target=loop1, args=("常大仙",))
    t1.start()
    t2 = threading.Thread(target=loop2, args=("常小灵", "常小莹"))
    t2.start()

    print("ALL done at:", time.ctime()

if __name__ == "__main__":
    main()
    # 一定要有 while 语句
    # 因为启动多线程后本程序就作为主程序存在
    # 如果多线程执行完毕, 则子程序可能也需要终止
    while True:
        time.sleep(10)