"""
79. 单词搜索
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。



示例 1：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true
示例 3：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false


提示：

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board 和 word 仅由大小写英文字母组成


进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？
"""
class Solution:
    direct = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 四个可能的方向上右下左
    col, row = 0, 0
    visited = list()

    def __inArea(self, x, y):
        return 0 <= x < self.row and 0 <= y < self.col

    # 从board[startx, starty]开始，寻找word[index:]
    def __searchWord(self, board, word, index, startx, starty):
        if index == len(word) - 1:
            return board[startx][starty] == word[index]

        if board[startx][starty] == word[index]:
            self.visited[startx][starty] = True
            # 从startx,starty出发，向四个方向寻找
            for i in range(4):
                newx = startx + self.direct[i][0]
                newy = starty + self.direct[i][1]
                if self.__inArea(newx, newy) and (not self.visited[newx][newy]):
                    if self.__searchWord(board, word, index+1, newx, newy):
                        return True
            self.visited[startx][starty] = False
        return False

    def exist(self, board: list, word: str) -> bool:
        self.row = len(board)
        self.col = len(board[0])
        self.visited = [[False] * self.col for _ in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                if self.__searchWord(board, word, 0, i, j):
                    return True
        return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    s = Solution()
    k = s.exist(board, word)
    print(k)
