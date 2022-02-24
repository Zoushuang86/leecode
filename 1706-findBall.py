"""
1706. 球会落何处
用一个大小为 m x n 的二维网格 grid 表示一个箱子。你有 n 颗球。箱子的顶部和底部都是开着的。

箱子中的每个单元格都有一个对角线挡板，跨过单元格的两个角，可以将球导向左侧或者右侧。

将球导向右侧的挡板跨过左上角和右下角，在网格中用 1 表示。
将球导向左侧的挡板跨过右上角和左下角，在网格中用 -1 表示。
在箱子每一列的顶端各放一颗球。每颗球都可能卡在箱子里或从底部掉出来。如果球恰好卡在两块挡板之间的 "V" 形图案，或者被一块挡导向到箱子的任意一侧边上，就会卡住。

返回一个大小为 n 的数组 answer ，其中 answer[i] 是球放在顶部的第 i 列后从底部掉出来的那一列对应的下标，如果球卡在盒子里，则返回 -1 。



示例 1：



输入：grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
输出：[1,-1,-1,-1,-1]
解释：示例如图：
b0 球开始放在第 0 列上，最终从箱子底部第 1 列掉出。
b1 球开始放在第 1 列上，会卡在第 2、3 列和第 1 行之间的 "V" 形里。
b2 球开始放在第 2 列上，会卡在第 2、3 列和第 0 行之间的 "V" 形里。
b3 球开始放在第 3 列上，会卡在第 2、3 列和第 0 行之间的 "V" 形里。
b4 球开始放在第 4 列上，会卡在第 2、3 列和第 1 行之间的 "V" 形里。
示例 2：

输入：grid = [[-1]]
输出：[-1]
解释：球被卡在箱子左侧边上。
示例 3：

输入：grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
输出：[0,1,2,3,4,-1]


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] 为 1 或 -1
"""
class Solution:
    """
    模拟：按行
    执行用时：60 ms, 在所有 Python3 提交中击败了41.84%的用户
    内存消耗：15.3 MB, 在所有 Python3 提交中击败了62.25%的用户
    """
    def findBall(self, grid: list) -> list:
        m, n = len(grid), len(grid[0])
        col = [k for k in range(n)]
        for i in range(m):
            for j in range(n):
                # 已经被判断被卡住
                if col[j] == -1:
                    continue

                # 判断是否还会继续落下
                # 被卡在边缘
                if (col[j] == 0 and grid[i][col[j]] == -1) or (col[j] == n-1 and grid[i][col[j]] == 1):
                    col[j] = -1
                else:
                    if grid[i][col[j]] == 1:
                        if grid[i][col[j]+1] == 1:
                            col[j] += 1
                        else:
                            col[j] = -1
                    else:
                        if grid[i][col[j]-1] == -1:
                            col[j] -= 1
                        else:
                            col[j] = -1
        return col
    """
    模拟：按每一个小球
    会更快点，提前终止了已经卡住的小球
    执行用时：52 ms, 在所有 Python3 提交中击败了74.49%的用户
    内存消耗：15.3 MB, 在所有 Python3 提交中击败了71.43%的用户
    
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        ans = [-1] * n
        for j in range(n):
            col = j  # 球的初始列
            for row in grid:
                dir = row[col]
                col += dir  # 移动球
                if col < 0 or col == n or row[col] != dir:  # 到达侧边或 V 形
                    break
            else:  # 成功到达底部
                ans[j] = col
        return ans
    """

if __name__ == "__main__":
    grid = [[-1]]
    s = Solution()
    print(s.findBall(grid))
