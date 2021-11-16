"""
37. 解数独
编写一个程序，通过填充空格来解决数独问题。

数独的解法需 遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
数独部分空格内已填入了数字，空白格用 '.' 表示。



示例：


输入：board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
输出：[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
解释：输入的数独如上图所示，唯一有效的解决方案如下所示：




提示：

board.length == 9
board[i].length == 9
board[i][j] 是一位数字或者 '.'
题目数据 保证 输入数独仅有一个解
"""
class Solution:
    valid = False

    def solveSudoku(self, board: list) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        row_set = [set() for _ in range(row)]
        col_set = [set() for _ in range(col)]
        gird_set = list()
        for _ in range(3):
            gird_set.append([set(), set(), set()])
        self.valid = False
        spaces = list()
        for i in range(row):
            for j in range(col):
                e = board[i][j]
                if e != '.':
                    row_set[i].add(e)
                    col_set[j].add(e)
                    gird_set[i//3][j//3].add(e)
                else:
                    spaces.append([i, j])

        def __dfs(cur):
            if len(spaces) == cur:
                self.valid = True
                return

            i, j = spaces[cur]
            for e in range(1, 10):
                e = str(e)
                if e not in row_set[i] and e not in col_set[j] and e not in gird_set[i//3][j//3]:
                    board[i][j] = e
                    row_set[i].add(e)
                    col_set[j].add(e)
                    gird_set[i // 3][j // 3].add(e)
                    __dfs(cur+1)
                    row_set[i].remove(e)
                    col_set[j].remove(e)
                    gird_set[i // 3][j // 3].remove(e)
                if self.valid:
                    return

        self.valid = False
        __dfs(0)
        for k in board:
            print(k)


if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    s = Solution()
    res = s.solveSudoku(board)
    print(res)
