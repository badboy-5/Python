# -*- coding: utf-8 -*-
# @File  : 9.py
# @Time : 3/22/2020
# @Software: PyCharm
# @Author: Bad
# @DESC:使用循环语句输出由*号组成的直角三角形(思考：怎么输出等腰三角形和菱形？)

high = int(input('Please input high:'))
s = 0
for i in range(0,high):
    for j in range(0,i):
        print('*',end="")
    print('*')
# for i in range(1,11):
#     s = ""
#     for j in range(0,i):
#         s += "*"
#     print(s)