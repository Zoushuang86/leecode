"""
剑指 Offer 03. 数组中重复的数字
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3


限制：

2 <= n <= 100000
"""
from collections import Counter

class Solution:
    """
    方法一：60ms

    def findRepeatNumber(self, nums: list) -> int:
        dic = Counter(nums)
        for k, v in dic.items():
            if v > 1:
                return k
        return -1
    """
    # 40ms
    def findRepeatNumber(self, nums: list) -> int:
        s = set()
        for e in nums:
            if e not in s:
                s.add(e)
            else:
                return e
        return -1
