"""
52. N皇后 II
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。



示例 1：


输入：n = 4
输出：2
解释：如上图所示，4 皇后问题存在两个不同的解法。
示例 2：

输入：n = 1
输出：1


提示：

1 <= n <= 9
皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
"""
class Solution:
    res = 0
    col = list()
    dia1 = list()
    dia2 = list()

    # 尝试在一个n皇后问题中，摆放第index行的皇后位置
    def __putQueue(self, n, index, row):
        if index == n:
            self.res += 1
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

    def totalNQueens(self, n: int) -> int:
        self.res = 0
        self.col = [False for _ in range(n)]
        self.dia1 = [False for _ in range(2*n-1)]
        self.dia2 = [False for _ in range(2 * n - 1)]
        row = list()
        self.__putQueue(n, 0, row)
        return self.res


if __name__ == "__main__":
    n = 4
    s = Solution()
    res = s.totalNQueens(n)
    print(res)
