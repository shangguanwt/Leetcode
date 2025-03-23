#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject2 
@File    ：509.斐波那契数
@IDE     ：PyCharm 
@Author  ：shangguan
@Date    ：2025/3/23 17:56 
'''
class Solution:
    def fib(self, n: int) -> int:
        a,b=0,1
        if(n==0):
            return a
        else:
            for _ in range(n-1):
                a,b=b,a+b
            return b
if __name__=="__main__":
    method = Solution()
    a = int(input("输入一个数：\n"))
    print(method.fib(a))