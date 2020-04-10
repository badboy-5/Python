# -*- coding: utf-8 -*-
# @File  : 01.py
# @Time : 2020/4/10
# @Software: PyCharm
# @Author: Bad
# @DESC:# -*- coding: utf-8 -*-
# # @File  : 01.py
# # @Time : 2020/4/10
# # @Software: PyCharm
# # @Author: Bad
# # @DESC:有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数?都是多少?

c = 0

print('能组成一下数字：')

for i in range(1,5):
    for a in range(1,5):
        for b in range(1,5):
            if i != a and a != b and i != b:
                print('%d%d%d'%(i,a,b))
                c += 1
print('共组成%d个互不相同且无重复数字的三位数'%c)