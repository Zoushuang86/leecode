"""
1447. 最简分数
给你一个整数 n ，请你返回所有 0 到 1 之间（不包括 0 和 1）满足分母小于等于  n 的 最简 分数 。
分数可以以 任意 顺序返回。



示例 1：

输入：n = 2
输出：["1/2"]
解释："1/2" 是唯一一个分母小于等于 2 的最简分数。
示例 2：

输入：n = 3
输出：["1/2","1/3","2/3"]
示例 3：

输入：n = 4
输出：["1/2","1/3","1/4","2/3","3/4"]
解释："2/4" 不是最简分数，因为它可以化简为 "1/2" 。
示例 4：

输入：n = 1
输出：[]


提示：

1 <= n <= 100
"""
"""
执行用时：88 ms, 在所有 Python3 提交中击败了67.65%的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了46.08%的用户
"""
import math

"""
    def gcd(x, y):
        while (y):
            x, y = y, x % y
        return x

"""
class Solution:
    def simplifiedFractions(self, n: int) -> list:
        res = []
        for i in range(2, n+1):
            for j in range(1, i):
                if math.gcd(i, j) == 1: # a和b的最高公约数
                    res.append(str(j)+'/'+str(i))
        return res


if __name__ == "__main__":
    n = 10
    s = Solution()
    print(s.simplifiedFractions(n))
