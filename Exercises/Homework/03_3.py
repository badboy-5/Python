# -*- coding: utf-8 -*-
# @File  : 03_3.py
# @Time : 2020/4/10
# @Software: PyCharm
# @Author: Bad
# @DESC:
# 游戏:允许用户输入一个数字，进行年龄的正确匹配。
#       ③、次数限制匹配----程序员给定循环的次数

true_age = 21
times = 3

for i in range(1,4):
    input_age = int(input('请输入你猜测的年龄：'))
    times = times-1
    if input_age == true_age:
        print('You Are Right!')
        break
    elif input_age != true_age:
        if times == 0:
            print('Game Failed!')
        else:
            print('You Are Wrong!You have %d chance!'%times)
