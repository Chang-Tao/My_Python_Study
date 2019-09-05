# 猜数字

def guess():
    g: int = 55
    s = 5
    r = True
    while r:
        n = int(input("请输入数字: "))
        if n == g:
            print("猜对了~~~!")
            break
        elif n < g:
            print("小了小了~~~!")
            s -= 1
            if s == 0:
                print("游戏结束!!")
                break
        elif n > g:
            print("大了大了~!!")
            s -= 1
            if s == 0:
                print("游戏结束!!")
                break


guess()
