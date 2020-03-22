# -*- coding: utf-8 -*-
# @File  : 2.py
# @Time : 3/21/2020
# @Software: PyCharm
# @Author: Bad
# @DESC:使用Python编程，求1~100间所有偶数的和。

sum = 0
for i in range(1,101):
    if i % 2 == 0:
        sum += i
print(sum)
