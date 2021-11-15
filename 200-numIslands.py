"""
200. 岛屿数量
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。



示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'
"""
class Solution:
    direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 四个可能的方向上右下左
    col, row = 0, 0
    visited = list()

    def __inArea(self, x, y):
        return 0 <= x < self.row and 0 <= y < self.col

    # 从grid[i][j]开始进行floorfill
    def __dfs(self, grid, i, j):
        self.visited[i][j] = True
        for index in range(4):
            x = i + self.direct[index][0]
            y = j + self.direct[index][1]
            if self.__inArea(x, y) and not self.visited[x][y] and grid[x][y] == '1':
                self.__dfs(grid, x, y)
        return

    def numIslands(self, grid: list) -> int:
        self.row = len(grid)
        if self.row == 0:
            return 0
        self.col = len(grid[0])
        self.visited = [[False] * self.col for _ in range(self.row)]

        res = 0
        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j] == '1' and not self.visited[i][j]:
                    res += 1
                    self.__dfs(grid, i, j)

        return res


if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    s = Solution()
    k = s.numIslands(grid)
    print(k)
