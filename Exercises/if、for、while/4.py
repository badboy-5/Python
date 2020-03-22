# -*- coding: utf-8 -*-
# @File  : 4.py
# @Time : 3/21/2020
# @Software: PyCharm
# @Author: Bad
# @DESC:
# 用Python编写程序，输入一年份，判断该年份是否是闰年并输出结果。
# 注:凡符合下面两个条件之一的年份是闰年。
# 	a)能被4整除但不能被100整除。
# 	b)能被400整除。

year = int(input("Please input year:"))

if year % 4 == 0 and year % 100 != 0:
    print('%d is a leap year!'%year)
elif year % 400 == 0:
    print('%d is a leap year!'%year)
else:
    print('%d is a nonleap year!'%year)