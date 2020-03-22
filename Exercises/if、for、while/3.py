# -*- coding: utf-8 -*-
# @File  : 3.py
# @Time : 3/21/2020
# @Software: PyCharm
# @Author: Bad
# @DESC:从键盘接收一个百分制成绩(0~100),要求输出其对应的成绩等级A~E。其中，90分以上为A，80~89分为B，70~79分为C，60~69分为D，60 分以下为E。

grade = int(input("Please input your grade:"))

if 0 <= grade <= 100:
    if grade >= 90:
        print('A')
    elif grade >= 80:
        print('B')
    elif grade >= 70:
        print('C')
    elif grade >= 60:
        print('D')
    else:
        print('E')
else:
    print('Input error!')