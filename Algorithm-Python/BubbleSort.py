# coding:utf-8
# Author: Neacik

def bubblesort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
    return alist


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(bubblesort(alist))


def modbubblesort(alist):
    exchange = True
    passnum = len(alist) - 1
    while passnum >= 1 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                exchange = True
        passnum = passnum - 1
    return alist


print(modbubblesort(alist))
