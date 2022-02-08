"""
1001. 网格照明
在大小为 n x n 的网格 grid 上，每个单元格都有一盏灯，最初灯都处于 关闭 状态。

给你一个由灯的位置组成的二维数组 lamps ，其中 lamps[i] = [rowi, coli] 表示 打开 位于 grid[rowi][coli] 的灯。即便同一盏灯可能在 lamps 中多次列出，不会影响这盏灯处于 打开 状态。

当一盏灯处于打开状态，它将会照亮 自身所在单元格 以及同一 行 、同一 列 和两条 对角线 上的 所有其他单元格 。

另给你一个二维数组 queries ，其中 queries[j] = [rowj, colj] 。对于第 j 个查询，如果单元格 [rowj, colj] 是被照亮的，则查询结果为 1 ，否则为 0 。在第 j 次查询之后 [按照查询的顺序] ，关闭 位于单元格 grid[rowj][colj] 上及相邻 8 个方向上（与单元格 grid[rowi][coli] 共享角或边）的任何灯。

返回一个整数数组 ans 作为答案， ans[j] 应等于第 j 次查询 queries[j] 的结果，1 表示照亮，0 表示未照亮。



示例 1：


输入：n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
输出：[1,0]
解释：最初所有灯都是关闭的。在执行查询之前，打开位于 [0, 0] 和 [4, 4] 的灯。第 0 次查询检查 grid[1][1] 是否被照亮（蓝色方框）。该单元格被照亮，所以 ans[0] = 1 。然后，关闭红色方框中的所有灯。

第 1 次查询检查 grid[1][0] 是否被照亮（蓝色方框）。该单元格没有被照亮，所以 ans[1] = 0 。然后，关闭红色矩形中的所有灯。

示例 2：

输入：n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]]
输出：[1,1]
示例 3：

输入：n = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]
输出：[1,1,0]


提示：

1 <= n <= 109
0 <= lamps.length <= 20000
0 <= queries.length <= 20000
lamps[i].length == 2
0 <= rowi, coli < n
queries[j].length == 2
0 <= rowj, colj < n
"""
"""
超时

class Solution:
    def upgradeGrid(self, grid: list, row, col, n, light=True):
        upgrade = [[row, col]]

        # 同行
        for j in range(n):
            if j != col:
                upgrade.append([row, j])

        # 同列
        for i in range(n):
            if i != row:
                upgrade.append([i, col])

        # 主对角线
        main = row - col
        for k in range(n):
            new_col = k - main
            if 0 <= new_col < n:
                if k != row and new_col != col:
                    upgrade.append([k, new_col])

        # 斜对角线
        sub = row + col
        for q in range(n):
            new_col = sub - q
            if 0 <= new_col < n:
                if q != row and new_col != col:
                    upgrade.append([q, new_col])

        # 更新grid
        for g in upgrade:
            if light:
                grid[g[0]][g[1]].append([row, col])
            else:
                grid[g[0]][g[1]].remove([row, col])

        return grid

    def gridIllumination(self, n: int, lamps: list, queries: list) -> list:
        lamp = [[0] * n for _ in range(n)]
        for i in lamps:
            lamp[i[0]][i[1]] = 1

        res = []
        grid = [[[] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if lamp[i][j] == 1:
                    grid = self.upgradeGrid(grid, i, j, n, light=True)

        for _, (row, col) in enumerate(queries):
            # 判断格子是否被照亮
            if len(grid[row][col]) > 0:
                res.append(1)
            else:
                res.append(0)

            # 判断需要关闭的灯
            close = []
            for i in range(-1, 2):
                new_row = row + i
                if 0 <= new_row < n:
                    for j in range(-1, 2):
                        new_col = col + j
                        if 0 <= new_col < n:
                            if lamp[new_row][new_col] == 1:
                                lamp[new_row][new_col] = 0
                                close.append([new_row, new_col])

            # 更新grid
            for c in close:
                grid = self.upgradeGrid(grid, c[0], c[1], n, light=False)

        return res
"""
from collections import defaultdict

# 修改记录是否被照亮的方式
"""
执行用时：464 ms, 在所有 Python3 提交中击败了11.11%的用户
内存消耗：34.5 MB, 在所有 Python3 提交中击败了52.78%的用户
"""
class Solution:
    def gridIllumination(self, n: int, lamps: list, queries: list) -> list:
        points = set()
        row, col, diagonal, antiDiagonal = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)
        for r, c in lamps:
            if (r, c) in points:
                continue
            points.add((r, c))
            row[r] += 1
            col[c] += 1
            diagonal[r-c] += 1
            antiDiagonal[r+c] += 1

        ans = [0 for _ in range(len(queries))]
        for i, (r, c) in enumerate(queries):
            if row[r] or col[c] or diagonal[r-c] or antiDiagonal[r+c]:
                ans[i] = 1
            for x in range(r-1, r+2):
                for y in range(c-1, c+2):
                    if x < 0 or y < 0 or x >= n or y >= n or (x, y) not in points:
                        continue
                    points.remove((x, y))
                    row[x] -= 1
                    col[y] -= 1
                    diagonal[x-y] -= 1
                    antiDiagonal[x+y] -= 1
        return ans


if __name__ == "__main__":
    n = 6
    lamps = [[2,5],[4,2],[0,3],[0,5],[1,4],[4,2],[3,3],[1,0]]
    queries = [[4,3],[3,1],[5,3],[0,5],[4,4],[3,3]]
    s = Solution()
    print(s.gridIllumination(n, lamps, queries))
