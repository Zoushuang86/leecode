"""
130. 被围绕的区域
给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，
并将这些区域里所有的 'O' 用 'X' 填充。

示例 1：


输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
示例 2：

输入：board = [["X"]]
输出：[["X"]]


提示：

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] 为 'X' 或 'O'
"""
"""
class Solution:
    direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 四个可能的方向上右下左
    col, row = 0, 0
    visited = list()
    grid = list()

    def __inArea(self, x, y):
        return 0 <= x < self.row and 0 <= y < self.col

    # 从grid[i][j]开始进行floorfill
    def __dfs(self, i, j):
        self.grid[i][j] = 'A'
        self.visited[i][j] = True
        for index in range(4):
            x = i + self.direct[index][0]
            y = j + self.direct[index][1]
            if self.__inArea(x, y) and not self.visited[x][y] and grid[x][y] == 'O':
                self.__dfs(x, y)

    def solve(self, grid) -> None:
        self.grid = grid
        self.row = len(self.grid)
        self.col = len(self.grid[0])
        self.visited = [[False] * self.col for _ in range(self.row)]

        for i in range(self.row):
            for j in [0, self.col-1]:
                if self.grid[i][j] == 'O' and not self.visited[i][j]:
                    self.__dfs(i, j)
        for i in [0, self.row-1]:
            for j in range(self.col):
                if self.grid[i][j] == 'O' and not self.visited[i][j]:
                    self.__dfs(i, j)

        print(self.grid)
        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j] == 'A':
                    self.grid[i][j] = 'O'
                elif self.grid[i][j] == 'O':
                    self.grid[i][j] = 'X'
        print(self.grid)
"""
class Solution:
    def solve(self, board) -> None:
        direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        row = len(board)
        col = len(board[0])
        visited = [[False] * col for _ in range(row)]

        def __inArea(x, y):
            return 0 <= x < row and 0 <= y < col

        # board[i][j]开始进行floorfill
        def __dfs(i, j):
            board[i][j] = 'A'
            visited[i][j] = True
            for index in range(4):
                x = i + direct[index][0]
                y = j + direct[index][1]
                if __inArea(x, y) and not visited[x][y] and board[x][y] == 'O':
                    __dfs(x, y)

        for i in range(row):
            for j in [0, col-1]:
                if board[i][j] == 'O' and not visited[i][j]:
                    __dfs(i, j)
        for i in [0, row-1]:
            for j in range(col):
                if board[i][j] == 'O' and not visited[i][j]:
                    __dfs(i, j)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


if __name__ == "__main__":
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    s = Solution()
    s.solve(board)
