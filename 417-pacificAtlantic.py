"""
417. 太平洋大西洋水流问题
给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，
而“大西洋”处于大陆的右边界和下边界。

规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。

请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。



提示：

输出坐标的顺序不重要
m 和 n 都小于150


示例：



给定下面的 5x5 矩阵:

  太平洋 ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * 大西洋

返回:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).
"""
class Solution:
    def pacificAtlantic(self, heights: list) -> list:
        direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        row = len(heights)
        col = len(heights[0])
        pacific = [[0] * col for _ in range(row)]
        atlantic = [[0] * col for _ in range(row)]

        def __inArea(x, y):
            return 0 <= x < row and 0 <= y < col

        def __dfs(i, j, flagPacific):
            if visited[i][j] == 1:
                return

            visited[i][j] = 1
            if flagPacific:
                pacific[i][j] = 1
            else:
                atlantic[i][j] = 1

            for index in range(4):
                newx = i + direct[index][0]
                newy = j + direct[index][1]
                if __inArea(newx, newy) and heights[i][j] <= heights[newx][newy]:
                    __dfs(newx, newy, flagPacific)
            return

        # 左上方太平洋逆流
        visited = [[0] * col for _ in range(row)]
        for i in range(1):
            for j in range(col):
                __dfs(i, j, True)

        visited = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(1):
                __dfs(i, j, True)

        # 右下方大西洋逆流
        visited = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col-1, col):
                __dfs(i, j, False)

        visited = [[0] * col for _ in range(row)]
        for i in range(row-1, row):
            for j in range(col):
                __dfs(i, j, False)

        res = list()
        for i in range(row):
            for j in range(col):
                if pacific[i][j] == 1 and atlantic[i][j] == 1:
                    res.append([i, j])
        return res


if __name__ == "__main__":
    # board = [[1, 2, 2, 3, 5],
    #          [3, 2, 3, 4, 4],
    #          [2, 4, 5, 3, 1],
    #          [6, 7, 1, 4, 5],
    #          [5, 1, 1, 2, 4]]
    board = [[1,2,3],[8,9,4],[7,6,5]]
    s = Solution()
    print(s.pacificAtlantic(board))
