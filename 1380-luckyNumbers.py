"""
1380. 矩阵中的幸运数
给你一个 m * n 的矩阵，矩阵中的数字 各不相同 。请你按 任意 顺序返回矩阵中的所有幸运数。

幸运数是指矩阵中满足同时下列两个条件的元素：

在同一行的所有元素中最小
在同一列的所有元素中最大


示例 1：

输入：matrix = [[3,7,8],[9,11,13],[15,16,17]]
输出：[15]
解释：15 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。
示例 2：

输入：matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
输出：[12]
解释：12 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。
示例 3：

输入：matrix = [[7,8],[1,2]]
输出：[7]


提示：

m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 10^5
矩阵中的所有元素都是不同的
"""
class Solution:
    def luckyNumbers (self, matrix: list) -> list:
        m, n = len(matrix), len(matrix[0])

        minSet = set()
        for i in range(m):
            minSet.add(min(matrix[i]))
        maxSet = set()
        for j in range(n):
            maxTemp = matrix[0][j]
            for k in range(1, m):
                maxTemp = max(maxTemp, matrix[k][j])
            maxSet.add(maxTemp)
        return list(minSet & maxSet)


if __name__ == "__main__":
    nums = [[7,8],[1,2]]
    s = Solution()
    print(s.luckyNumbers(nums))
