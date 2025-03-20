#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@File    ：70.爬楼梯.py
@IDE     ：PyCharm 
@Author  ：shangguan
@Date    ：2025/3/20 16:07 
'''
class solution:

    def climbstep(self,n:int) -> int:
        a,b = 1,1
        for _ in range(n-1):
            a,b=b,a+b
        return b
if __name__=='__main__':
    ##方法一：创建实例，要不然无法引用类里面的方法
    sol = solution()
    a = int(input("输入要达到第几阶台阶"))

