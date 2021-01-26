"""
289. 生命游戏
根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。

给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。给你 m x n 网格面板 board 的当前状态，返回下一个状态。



示例 1：


输入：board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
输出：[[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
示例 2：


输入：board = [[1,1],[1,0]]
输出：[[1,1],[1,1]]


提示：

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] 为 0 或 1


进阶：

你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使用它们的更新后的值再更新其他格子。
本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。你将如何解决这些问题？
"""

"""
方法一：复制样本
执行用时：40 ms, 在所有 Python3 提交中击败了65.34%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了24.82%的用户

import copy
class Solution:
    def gameOfLife(self, board):
        #Do not return anything, modify board in-place instead.
        alive_board = copy.deepcopy(board)
        row_len = len(board)
        col_len = len(board[0])

        def calculate(i, j):
            alive = 0
            for row in [-1, 0, 1]:
                for col in [-1, 0, 1]:
                    # if (i+row >= 0) and (j+col >= 0) and (i+row < row_len) and (j+col < col_len):
                    # 比下一行慢了4ms
                    if (0 <= i+row < row_len) and (0 <= j+col < col_len):
                        alive += alive_board[i+row][j+col]
            alive = alive - alive_board[i][j]
            if board[i][j] == 1:
                if alive == 2 or alive == 3:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
            else:
                if alive == 3:
                    board[i][j] = 1

        for r in range(row_len):
            for c in range(col_len):
                calculate(r, c)
        return board
"""

"""
方法二：状态转换+位运算
执行用时：32 ms, 在所有 Python3 提交中击败了96.21%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了15.03%的用户
"""
class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                cnt = self.count_alive(board, i, j)
                if board[i][j] and cnt in [2, 3]:
                    board[i][j] = 3
                if not board[i][j] and cnt == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1

    def count_alive(self, board, i, j):
        m, n = len(board), len(board[0])
        cnt = 0
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dx, dy in directions:
            x, y = i + dx, j + dy
            if x < 0 or y < 0 or x == m or y == n:
                continue
            cnt += board[x][y] & 1

        return cnt


if __name__ == "__main__":
    A = [[1,1],[1,0]]
    s = Solution()
    print(s.gameOfLife(A))

