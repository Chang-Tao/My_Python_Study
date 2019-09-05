# 定义一个函数

def SayHello(name):
    print("我想要对你说爱你, {0}".format(name))
    print("你好, {0}".format(name))
    print("完成!......")


if __name__ == "__main__":
    print('***' * 10)
    name = input("请输入你的名字: ")
    print(SayHello(name=name))
    print('@@@' * 10)
