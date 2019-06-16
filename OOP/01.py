'''
定义一个学生类,用来形容一个学生
'''
class Student():
    # 一个空类, pass表示跳过,必须有
    pass

# 定义一个对象
mingyue = Student()

# 在定义一个类, 用来描述听python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    # 注意 def doHomework的缩进层级
    # 默认有一个self参数
    def doHomework(self):
        print("我在写作业")

        # 在函数末尾使用return语句
        return None

# 实例化一个叫yueyue的学生, 是一个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
# 成员函数的调用没有传递参数
yueyue.doHomework()