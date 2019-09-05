# 包含一个学生类和一个 sayHello 函数
# 一个打印语句

class Student(object):
    def __init__(self, name="NoName", age=18):
        self.name = name
        self.age = age

    def say(self):
        print("我的名字叫{}".format(self.name))


def sayHello():
    print("欢迎来到灵煞科技公司")


# 此判断语句建议作为程序的入口
if __name__ == '__main__':
    print("我是模块p01, 叫我干啥!!!")
