"""
447. 回旋镖的数量
给定平面上 n 对 互不相同 的点 points ，其中 points[i] = [xi, yi] 。回旋镖 是由点 (i, j, k) 表示的元组 ，其中 i 和 j 之间的距离和 i 和 k 之间的欧式距离相等（需要考虑元组的顺序）。

返回平面上所有回旋镖的数量。


示例 1：

输入：points = [[0,0],[1,0],[2,0]]
输出：2
解释：两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
示例 2：

输入：points = [[1,1],[2,2],[3,3]]
输出：2
示例 3：

输入：points = [[1,1]]
输出：0
"""
class Solution:
    # 时间复杂度O(n^2)
    # 空间复杂度O(n)
    def numberOfBoomerangs(self, points):
        def dis(i, j):
            # 避免小数点，直接返回平方
            return (i[0] - j[0]) * (i[0] - j[0]) \
                   + (i[1] - j[1]) * (i[1] - j[1])

        res = 0
        for i in points:
            record = {}
            for j in points:
                distance = dis(i, j)
                if record.get(distance) == None:
                    record[distance] = 1
                else:
                    record[distance] += 1
            for value in record.values():
                res += value * (value - 1)
        return res


if __name__ == "__main__":
    points = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
    print(Solution().numberOfBoomerangs(points))
