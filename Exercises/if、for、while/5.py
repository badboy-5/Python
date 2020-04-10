# -*- coding: utf-8 -*-
# @File  : 5.py
# @Time : 3/21/2020
# @Software: PyCharm
# @Author: Bad
# @DESC:用Python编程，假设一年期定期利率为3.25%，计算一下需要过多少年，一万元的一年定期存款连本带息能翻番?
# 利息=本金*利率*时间

capital = 10000
year = 0

while capital < 20000:
    year += 1
    capital += (capital * 0.0325*1)
print('需要过%d年，一万元的一年定期存款连本带息能翻番'%year)

