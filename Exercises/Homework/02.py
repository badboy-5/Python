# -*- coding: utf-8 -*-
# @File  : 02.py
# @Time : 2020/4/10
# @Software: PyCharm
# @Author: Bad
# @DESC:球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米?第10次反弹多高?

path = 0
high =100

for i in range(1,11):
    if i >= 2:
        path += 2*high
    elif i < 2:
        path += high
    high = high/2
print('它在第10次落地时，共经过%d米'%path)
print('第10次反弹%d米'%high)
