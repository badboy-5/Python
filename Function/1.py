# -*- coding: utf-8 -*-
# @File  : 1.py
# @Time : 2020/5/8
# @Software: PyCharm
# @Author: Bad
# @DESC:定义一个getMax( )函数，返回三个数（从键盘输入的整数）中的最大值

def getMax():
    num1 = int(input("请输入第一个数:"))
    num2 = int(input("请输入第二个数:"))
    num3 = int(input("请输入第三个数:"))

    m = 0
    if num1 > num2:
        m = num1
    else:
        m = num2

    if m > num3:
        return "三个数中最大的数是："+str(m)
    else:
        return "三个数中最大的数是："+str(num3)

print(getMax())