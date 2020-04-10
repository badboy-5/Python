# -*- coding: utf-8 -*-
# @File  : 03_2.py
# @Time : 2020/4/10
# @Software: PyCharm
# @Author: Bad
# @DESC:
# 游戏:允许用户输入一个数字，进行年龄的正确匹配。
#       ②、无限次数匹配---程序代码只执行一次

true_age = 21
flag = 0

while flag == 0:
    input_age = int(input('请输入你猜测的年龄：'))
    if input_age == true_age:
        print('You Are Right!')
        flag = 1
    elif input_age != true_age:
        print('You Are Wrong! Try Again!')
        flag = 0

