"""
69. x 的平方根
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。
"""
"""
执行用时：44 ms, 在所有 Python3 提交中击败了84.89%的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了6.51%的用户

import math
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        r = int(math.exp(0.5*math.log(x)))
        return r+1 if (r+1)**2 <= x else r
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                l = mid+1
                ans = mid
            else:
                r = mid-1
        return ans


if __name__ == "__main__":
    print(Solution().mySqrt(100000))
