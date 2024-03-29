# 环境
- xubuntu 16.04
- anaconda
- pycharm
- python 3.6
- https://www.cnblogs.com/jokerbj/p/7460260.html
- http://www.dabeaz.com/python/UnderstandingGIL.pdf

# 多线程 vs 多进程
- 程序: 一堆代码以文本形式存入一个文档
- 进程: 程序运行的状态
    - 包含地址空间, 内存, 数据栈等
    - 每个进程有自己完全独立的运行环境, 多进程共享数据是一个问题
- 线程
    - 一个进程的独立运行片段, 一个进程可以由多个线程
    - 轻量化的进程
    - 一个进程的多个线程间共享数据和上下文运行环境
    - 共享互斥问题
- 全局解释器锁(GIL)
    - Python 代码的执行是由 python 虚拟机进行控制
    - 在主循环中只能有一个控制线程在执行 

- Python 包
    - thread: 早期版本, python3.0 改版为 _thread
    - threading: 当前通用包
- 案例 01: 顺序执行,耗时比较长
- 案例 02: 该用多线程, 缩短总时间, 使用_thread
- 案例 03: 多线程, 传参数

- threading 的使用
    - 直接利用 threading.Thread 生成 Thread 实例
        1. t = threading.Thread(target=xxx, args=(xxx, ))
        2. t.start(): 启动多线程
        3. t.join(): 等到多线程执行完成
        4. 案例 04