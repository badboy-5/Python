# -*- coding: utf-8 -*-
# @File  : 03_1.py
# @Time : 2020/4/10
# @Software: PyCharm
# @Author: Bad
# @DESC:
# 游戏:允许用户输入一个数字，进行年龄的正确匹配。
#       ①、基本匹配----猜一次执行一次代码

true_age = 21
input_age = int(input('请输入你猜测的年龄：'))

if input_age == true_age:
    print('You Are Right!')
else:
    print('You Are Wrong!')