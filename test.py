
# 猜数字
print("-----感谢您使用灵煞Py小程序-----")
print("-------------猜数字-------------")

sum = 55
n = 6

while True:
    s = int(input("请输入数字: "))
    if s == sum:
        print("猜对啦~!!")
        break

    elif s < sum:
        print("猜错拉~!")
        n -= 1
        if n >= 1:
            print("还有{0}次机会".format(n))
        if n < 1:
            print("机会用完拉,再接再厉~!!")
            break


    elif s > sum:
        print("大啦大啦~!")
        n -= 1
        if n >= 1:
            print("还有{0}次机会".format(n))
        if n < 1:
            print("机会用完拉,再接再厉~!!")
            break