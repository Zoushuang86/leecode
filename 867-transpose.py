"""
867. 转置矩阵
给定一个矩阵 A， 返回 A 的转置矩阵。

矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。



示例 1：

输入：[[1,2,3],[4,5,6],[7,8,9]]
输出：[[1,4,7],[2,5,8],[3,6,9]]
示例 2：

输入：[[1,2,3],[4,5,6]]
输出：[[1,4],[2,5],[3,6]]


提示：

1 <= A.length <= 1000
1 <= A[0].length <= 1000
"""
"""
class Solution:
    def transpose(self, A):
        import numpy as np
        return np.asarray(A).transpose().tolist()
"""

"""
执行用时：92 ms, 在所有 Python3 提交中击败了49.87%的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了5.23%的用户
"""
class Solution:
    def transpose(self, A):
        res = []
        for i in range(len(A[0])):  # 列
            t = []
            for j in range(len(A)): # 行
                t.append(A[j][i])
            res.append(t)
        return res


if __name__ == "__main__":
    A = [[1,2,3],[4,5,6]]
    s = Solution()
    print(s.transpose(A))
