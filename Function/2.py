# -*- coding: utf-8 -*-
# @File  : 2.py
# @Time : 2020/5/11
# @Software: PyCharm
# @Author: Bad
# @DESC:定义一个函数，判断输入的三个数字是否能够构成三角形的三条边

def triangle():
    a = int(input("请输入三角形的一条边长："))
    b = int(input("请输入三角形的一条边长："))
    c = int(input("请输入三角形的一条边长："))

    if (a+b>c and a+c>b and b+c>a):
        if (a-b<c and a-c<b and b-c<a):
            return "这三条边可以构成三角形！"
    else:
        return "这三条边不能构成三角形！"

print(triangle())
