#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject2 
@File    ：1137.第N个泰波那契数
@IDE     ：PyCharm 
@Author  ：shangguan
@Date    ：2025/3/26 11:09 
'''


class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        if (n == 0):
            return 0
        for _ in range(n - 2):
            a, b, c = b, c, a + b + c
        return c


if __name__ == "__main__":
    method = Solution()
    a = int(input("输入一个数：\n"))
    print(method.tribonacci(a))