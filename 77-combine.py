"""
77. 组合
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。



示例 1：

输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
示例 2：

输入：n = 1, k = 1
输出：[[1]]


提示：

1 <= n <= 20
1 <= k <= n
"""
"""
class Solution:
    def combine(self, n: int, k: int) -> list:
        res = []
        vis = [False] * (n + 1)
        pre = []

        def dfs(start):
            if len(pre) == k:
                res.append(pre[:])
                return

            for i in range(start, n+1):
                if vis[i] == True:
                    return

                pre.append(i)
                vis[i] = True
                dfs(i+1)
                pre.pop()
                vis[i] = False

        dfs(1)
        return res
"""


class Solution:
    res = []

    def __generate_combinations(self, n, k, start, pre):
        if len(pre) == k:
            self.res.append(pre[:])
            return

        for i in range(start, n-(k-len(pre))+2):
            pre.append(i)
            self.__generate_combinations(n, k, i+1, pre)
            pre.pop()

    def combine(self, n: int, k: int) -> list:
        self.res.clear()
        if n <= 0 or k <= 0 or k > n:
            return self.res
        c = []
        self.__generate_combinations(n, k, 1, c)
        return self.res


if __name__ == "__main__":
    n = 4
    k = 2
    s = Solution()
    print(s.combine(n, k))
