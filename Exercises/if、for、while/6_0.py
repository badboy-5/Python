# -*- coding: utf-8 -*-
# @File  : 6_0.py
# @Time : 3/22/2020
# @Software: PyCharm
# @Author: Bad
# @DESC:

total = 1534
day = 1
while day <= 9:
    residue = (total/2)-1
    total = residue
    day += 1
print(total)