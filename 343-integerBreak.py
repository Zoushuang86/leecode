"""
343. 整数拆分
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。
"""
"""
记忆递归

class Solution:
    memo = list()

    def __breakInteger(self, n):
        if n == 1:
            return 1

        if self.memo[n] != -1:
            return self.memo[n]

        res = -1
        for i in range(1, n):
             res = max(i * self.__breakInteger(n-i), res, i * (n-i))
        self.memo[n] = res
        return res

    def integerBreak(self, n: int) -> int:
        self.memo = [-1 for _ in range(n+1)]
        return self.__breakInteger(n)
"""
class Solution:
    def integerBreak(self, n: int) -> int:
        memo = [-1 for _ in range(n+1)]
        memo[1] = 1
        for i in range(2, n+1):
            for j in range(1, i):
                memo[i] = max(j * (i-j), j * memo[i-j], memo[i])
        return memo[n]


if __name__ == "__main__":
    n = 10
    print(Solution().integerBreak(n))
