# -*- coding: utf-8 -*-
# @File  : 9_01.py
# @Time : 3/22/2020
# @Software: PyCharm
# @Author: Bad
# @DESC:使用循环语句输出由*号组成的等腰三角形

high = int(input("Please input high:"))

for i in range(0,high):
    space = ""
    for j in range(high-i,0,-1):
        space += " "
    print(space,end="")
    for h in range(0,2*i):
        print('*',end="")
    print('*')