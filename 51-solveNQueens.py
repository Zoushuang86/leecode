"""
51. N 皇后
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。



示例 1：


输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。
示例 2：

输入：n = 1
输出：[["Q"]]


提示：

1 <= n <= 9
皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
"""
class Solution:
    res = list()
    col = list()
    dia1 = list()
    dia2 = list()

    def __generateBoard(self, n, row):
        board = [['.'] * n for _ in range(n)]
        for i in range(n):
            board[i][row[i]:row[i]+1] = 'Q'
            board[i] = "".join(board[i])
        return board

    # 尝试在一个n皇后问题中，摆放第index行的皇后位置
    def __putQueue(self, n, index, row):
        if index == n:
            self.res.append(self.__generateBoard(n, row))
            return

        for i in range(n):
            if not self.col[i] and not self.dia1[index+i] and not self.dia2[index-i+n-1]:
                row.append(i)
                self.col[i] = True
                self.dia1[index+i] = True
                self.dia2[index-i+n-1] = True
                self.__putQueue(n, index+1, row)
                self.col[i] = False
                self.dia1[index + i] = False
                self.dia2[index - i + n - 1] = False
                row.pop()
        return

    def solveNQueens(self, n: int) -> list:
        self.res.clear()
        self.col = [False for _ in range(n)]
        self.dia1 = [False for _ in range(2*n-1)]
        self.dia2 = [False for _ in range(2 * n - 1)]
        row = list()
        self.__putQueue(n, 0, row)
        return self.res


if __name__ == "__main__":
    n = 8
    s = Solution()
    res = s.solveNQueens(n)
    for i in res:
        for j in i:
            print(j)
        print("\n")
