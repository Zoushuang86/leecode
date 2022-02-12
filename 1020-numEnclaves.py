"""
1020. 飞地的数量
给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。

一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。

返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。



示例 1：


输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
输出：3
解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
示例 2：


输入：grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
输出：0
解释：所有 1 都在边界上或可以到达边界。


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] 的值为 0 或 1
"""
"""
深度优先遍历DFS
执行用时：120 ms, 在所有 Python3 提交中击败了39.49%的用户
内存消耗：17.3 MB, 在所有 Python3 提交中击败了8.32%的用户

class Solution:
    def numEnclaves(self, grid) -> int:
        # 坐标上下左右移动
        move = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        m = len(grid)
        n = len(grid[0])
        enclaves = [[False for _ in range(n)] for _ in range(m)]

        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0 or enclaves[row][col]:
                    return
            enclaves[row][col] = True
            for offset in move:
                x = row + offset[0]
                y = col + offset[1]
                dfs(row + offset[0], col + offset[1])


        # 从第0列和第n-1列边界进行dfs
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)

        # 从第0行和第m-1行边界进行dfs
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)

        res = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j] == 1 and not enclaves[i][j]:
                    res += 1
        return res
"""
"""
广度优先遍历BFS
执行用时：100 ms, 在所有 Python3 提交中击败了50.35%的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了72.06%的用户
"""
from collections import deque

class Solution:
    def numEnclaves(self, grid: list) -> int:
        m, n = len(grid), len(grid[0])
        vis = [[False] * n for _ in range(m)]
        q = deque()
        for i, row in enumerate(grid):
            if row[0]:
                vis[i][0] = True
                q.append((i, 0))
            if row[n - 1]:
                vis[i][n - 1] = True
                q.append((i, n - 1))
        for j in range(1, n - 1):
            if grid[0][j]:
                vis[0][j] = True
                q.append((0, j))
            if grid[m - 1][j]:
                vis[m - 1][j] = True
                q.append((m - 1, j))
        while q:
            r, c = q.popleft()
            for x, y in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] and not vis[x][y]:
                    vis[x][y] = True
                    q.append((x, y))
        return sum(grid[i][j] and not vis[i][j] for i in range(1, m - 1) for j in range(1, n - 1))


if __name__ == "__main__":
    grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
    s = Solution()
    print(s.numEnclaves(grid))
