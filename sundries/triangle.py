# coding:utf-8
# Author: Neacik


def equilateral(n):
    for i in range(1, n + 1):
        print(' ' * (n - i), end='')
        print('* ' * (i) + '1')
    print("等边三角形")


def right1(n):
    tmp = 1
    while tmp <= n:
        width = tmp
        while width > 0:
            print("*", end="")
            width -= 1
        print("")
        tmp += 1
    print("直角三角形1")


def right2(n):
    while n > 0:
        tmp = n
        while tmp > 0:
            print("*",end="")
            tmp -= 1
        print("")
        n -= 1
    print("直角三角形2")


n = int(input('请输入边长：'))
equilateral(n)
right1(n)
right2(n)