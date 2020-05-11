# -*- coding: utf-8 -*-
# @File  : 3.py
# @Time : 2020/5/11
# @Software: PyCharm
# @Author: Bad
# @DESC:定义一个函数，求两个正整数的最小公倍数

def lcm():
    if a > b:
        big = a
    else:
        big = b
    while True:
        if (big % a == 0) and (big % b == 0):
            c = big
            break
        else:
            big += 1
    return c

a = int(input("请输入一个数："))
b = int(input("请输入另一个数:"))
print(a,"与",b,"的最小公倍数为：",lcm())

