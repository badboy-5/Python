# -*- coding: utf-8 -*-
# @File  : 6.py
# @Time : 3/22/2020
# @Software: PyCharm
# @Author: Bad
# @DESC:
# 编程，解决猴子吃桃问题。
# 猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个。第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想吃时，只剩下一个桃子了。求第一天共摘多少个桃子。(迭代法)。

day = 9
residue = 1
while day > 0:
    total = (residue + 1)*2
    residue = total
    day -= 1
print('第一天共摘%d个桃子！'%total)
print('吃死你吧！臭猴子！')

# day = 9
# total = 1
# while day > 0:
#     total = (total + 1)*2
#     day -= 1
# print('第一天共摘%d个桃子！'%total)
# print('吃死你吧！臭猴子！')