# -*- coding: utf-8 -*-
# @File  : 1.py
# @Time : 3/21/2020
# @Software: PyCharm
# @Author: Bad
# @DESC:编写一个python程序，完成输入两个数，比较它们的大小并输出其中较大者。

num1 = int(input("Please input num1:"))
num2 = int(input("Please input num2:"))

if num1 >= num2:
    max = num1
else:
    max = num2
print('The Max num is:%d'%max)