import time
import _thread as thread

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
    print("我是参数", in1, "和参数", in2)
    # 睡眠时间, 单位是秒(s)
    time.sleep(2)
    print("End loop 2 at:", time.ctime())


def main():
    print("Starting at:", time.ctime())
    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程函数为 start_new_thread
    # 参数两个, 一个是需要运行的函数名, dirge是函数的参数作为元组使用, 为空则使用空元祖
    # 注意: 如果函数只有一个参数, 需要参数后有一个逗号
    thread.start_new_thread(loop1,("常大仙", ))

    thread.start_new_thread(loop2,("常小灵", "常小莹"))

    print("ALL done at:", time.ctime())

if __name__ == "__main__":
    main()
    # 一定要有 while 语句
    # 因为启动多线程后本程序就作为主程序存在
    # 如果多线程执行完毕, 则子程序可能也需要终止
    while True:
        time.sleep(10)