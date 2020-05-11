# -*- coding: utf-8 -*-
# @File  : 4.py
# @Time : 2020/5/11
# @Software: PyCharm
# @Author: Bad
# @DESC:编写函数，可以接收任意多个整数并输出其中的最大值和所有整数之和

def function(*num):
    print("最大的数是：%d"%(max(num)))
    s = sum(num)
    print("所有整数之和为：%d"%s)
