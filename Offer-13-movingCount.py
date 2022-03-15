"""
剑指 Offer 13. 机器人的运动范围
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？



示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20
"""
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        dirct = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        vis = [[False] * n for _ in range(m)]
        maps = [i // 10 + i % 10 for i in range(max(n,m))]
        board = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if maps[i] + maps[j] <= k:
                    board[i][j] = True
        res = 0

        def check(x, y):
            return 0 <= x < m and 0 <= y < n

        def dfs(x, y):
            nonlocal res
            if board[x][y]:
                vis[x][y] = True
                res += 1
                for offsetx, offsety in dirct:
                    i, j = x + offsetx, y + offsety
                    if check(i, j) and not vis[i][j]:
                        dfs(i, j)

        dfs(0, 0)
        return res