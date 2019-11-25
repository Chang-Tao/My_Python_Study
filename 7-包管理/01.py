
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


print("我是模块01, 叫我干啥!!!")
