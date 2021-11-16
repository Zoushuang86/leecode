"""
70. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
"""

"""
滚动数组
执行用时：44 ms, 在所有 Python3 提交中击败了37.94%的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了9.11%的用户

class Solution:
    def climbStairs(self, n: int) -> int:
        p = 0
        q = 0
        r = 1
        for i in range(n):
            p = q
            q = r
            r = p + q
        return r
"""
"""
# 自上而下：递归
# 超时
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)
"""
"""
自下而上：动态规划
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        memo = [-1 for _ in range(n+1)]
        memo[0] = 1
        memo[1] = 1
        for i in range(2, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]


if __name__ == "__main__":
    print(Solution().climbStairs(5))
