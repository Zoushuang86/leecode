"""
149. 直线上最多的点数
给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。



示例 1：


输入：points = [[1,1],[2,2],[3,3]]
输出：3
示例 2：


输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出：4


提示：

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
points 中的所有点 互不相同
"""
"""
执行用时：60 ms, 在所有 Python3 提交中击败了53.31%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了67.40%的用户
"""
class Solution:
    def maxPoints(self, points):
        def slope(i,j):
            if j[0] == i[0]:
                return 'inf'
            else:
                return (j[1] - i[1]) / (j[0] - i[0])
        if len(points) < 2:
            return len(points)
        res = 0
        for i in points:
            record = {}
            for j in points:
                if i != j:
                    s = slope(i, j)
                    if record.get(s) == None:
                        record[s] = 1
                    else:
                        record[s] += 1
            for value in record.values():
                res = max(value+1, res)
        return res

"""
优化

最后我们再加四个小优化：

在点的总数量小于等于 2 的情况下，我们总可以用一条直线将所有点串联，此时我们直接返回点的总数量即可；
当我们枚举到点 i 时，我们只需要考虑编号大于 i 的点到点 i 的斜率，因为如果直线同时经过编号小于点 i 的点 j，那么当我们枚举到 j 时就已经考虑过该直线了；
当我们找到一条直线经过了图中超过半数的点时，我们即可以确定该直线即为经过最多点的直线；
当我们枚举到点 i（假设编号从 0 开始）时，我们至多只能找到 n−i 个点共线。假设此前找到的共线的点的数量的最大值为 k，如果有 k≥n−i，那么此时我们即可停止枚举，因为不可能再找到更大的答案了。

"""

if __name__ == "__main__":
    points = [[1,1],[2,2],[3,3]]
    print(Solution().maxPoints(points))
