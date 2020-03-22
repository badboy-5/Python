# -*- coding: utf-8 -*-
# @File  : 9_02.py
# @Time : 3/22/2020
# @Software: PyCharm
# @Author: Bad
# @DESC:使用循环语句输出由*号组成的菱形

high = int(input("Please input high:"))
#正等腰三角形
for i in range(0,high):
    space = ""
    for j in range(0,high-i):
        space += " "
    print(space,end="")
    for h in range(0,2*i):
        print('*',end="")
    print('*')
#倒等腰三角形
for i in range (0,high):
    space = ""
    for j in range(0,i+1):
        space += " "
    print(space,end="")
    for h in range(0,2*(high-i-1)):
        print('*',end="")
    print('*')