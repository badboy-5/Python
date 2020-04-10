# -*- coding: utf-8 -*-
# @File  : 03_4.py
# @Time : 2020/4/10
# @Software: PyCharm
# @Author: Bad
# @DESC:
# 游戏:允许用户输入一个数字，进行年龄的正确匹配。
#       ④、用户自行决定猜测的次数---由用户自己决定是否继续猜

true_age = 21
flag = 0

while flag == 0:
    input_age = int(input('请输入你猜测的年龄：'))
    if input_age == true_age:
        print('You Are Right!')
        break
    else:
        print('You Are Wrong!')
        a = input('Do you want to try again?(Y or N)')
        if 'N' in a:
            print('Game Failed!')
            break
        else:
            flag = 0