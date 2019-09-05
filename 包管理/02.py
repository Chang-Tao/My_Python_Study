# 借助于 importlib 包, 可以实现导入仪数字开头的模块名称
import importlib

# 相当于导入了一个叫 01 的模块并赋值给 lingsha
lingsha = importlib.import_module("01")


stu = lingsha.Student()
stu.say()
