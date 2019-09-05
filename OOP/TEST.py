# 定义一个 人 类

class Person(object):
    def __init__(self, name, np, age):
        self.name = name
        self.age = age
        self.np = np

    def Eat(self, name, np, age):
        print("{0}在吃饭".format(name))

    def Introduce(self, name, np, age):
        print("我叫{0}, 我来自{1}, 我今年{2}岁了.".format(name, np, age))


class Student(Person):
    def __init__(self):
        pass

    def Introduce(self, name, np, age):
        print("我叫{0}, 我今年{1}岁了, 我来自{2}".format(name, age, np))

    def Learning(self):
        print("今天学习数学!")



Ling = Student()
Ling.Introduce("灵儿", "安徽", 18)
Ling.Learning()